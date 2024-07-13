from snowflake.ml.modeling.metrics import (confusion_matrix,
                                        accuracy_score,
                                        f1_score, recall_score,
                                        precision_score,
                                        log_loss ,
                                        roc_auc_score ,
                                        roc_curve)

from snowflake.snowpark.functions import sqrt ,log, abs
import json

def generate_metrics(model, combined_df,model_type,true_cn,pred_cn,pred_proba):
    """
    Method to generate metrics
    """
    cls = None
    if model_type.lower() == "classification":
        pass
        cls = Classification(model, combined_df,model_type,true_cn,pred_cn,pred_proba)
    elif model_type.lower() == "regression":
        cls = Regression(model, combined_df,model_type,true_cn,pred_cn,pred_proba)
    return cls.get_metrics()
        

def try_or(fn):
    try:
        out = fn()
        return out
    except Exception as e:
        print(e)
        return None

def update_progress(progress):
    bar_length = 70
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
    if progress < 0:
        progress = 0
    if progress >= 1:
        progress = 1
    block = int(round(bar_length * progress))
    print("Calculating build time metrics\n")
    text = "Progress: {0} {1:.1f}%".format(
        "█" * block + " " * (bar_length - block), progress * 100
    )
    print(text)



class Regression:

    def __init__(self, model, sf_df,true_cn,pred_cn,pred_proba_cn):
        """
        Constructor to initialize the model object
        """
        self.model = model
        self.sf_df = sf_df 
        self.true_cn = true_cn
        self.pred_cn = pred_cn 
        self.pred_proba_cn = pred_proba_cn
        self.progress_base_value = 3
        self.progress_counter = 1 

    def get_metrics(self):
        """
        Method to get metrics 
        
        """
        all_summary = [
            self.cal_scatter_plot(),
            self.detailed_matrix(),
            #self.decision_tree(),
            self.cal_feature_importance(),
        ]
        return all_summary

    def cal_feature_importance(self):
        """
        Method to calculate variable importance
        """
        try:
            imp_list,feature_list,sklearn_model = [], None ,self.model
            if str(type(self.model)).find("snowflake") > 0:
                sklearn_model = self.model.to_sklearn()
                
            if hasattr(self.model,"feature_importances_"):
                feature_list = self.model.feature_importances_
            elif hasattr(self.model,"coef_"):
                feature_list = self.model.coef_
            else:
                pass
                
            for index , value in zip(sklearn_model.feature_names_in_,feature_list.tolist()):
                imp_list.append({"column_name": index, "importance": value})
                
        except Exception:
            imp_list = None
        feature_importance_dict = {
            "tag": "feature_importance",
            "model_metric_value": imp_list,
        }
        update_progress(self.progress_counter / self.progress_base_value)
        self.progress_counter += 1
        return feature_importance_dict

    def cal_scatter_plot(self):
        """
            Method is used to calculate the scatter plot
        """
        try:
            values_1  = self.sf_df.group_by([self.true_cn,self.pred_cn]).agg().limit(1000).collect()
            list1 = []
            for i,j in values_1:
                list1.append([i,j])
            scatt_dict = {"tag": "scatter_plot", "model_metric_value": list1}
            update_progress(self.progress_counter / self.progress_base_value)
            self.progress_counter += 1
            return scatt_dict
        except Exception as ex:
            print("Error while generating scatt plot")
    
    def detailed_matrix(self):
        
        """
        Method to calculate detailed matrix values of regression model
        """
        detailed_matrix_dict = {}
        import math
        from snowflake.ml.modeling.metrics import explained_variance_score, mean_absolute_percentage_error , mean_squared_error,mean_absolute_error,r2_score
        detailed_matrix_dict[explained_variance_score.__name__] = try_or(lambda : explained_variance_score(df=self.sf_df,y_true_col_names=self.true_cn, y_pred_col_names=self.pred_cn))
        detailed_matrix_dict[mean_absolute_percentage_error.__name__] = try_or(lambda : mean_absolute_percentage_error(df=self.sf_df,y_true_col_names=self.true_cn, y_pred_col_names=self.pred_cn))
        detailed_matrix_dict[mean_squared_error.__name__] = try_or(lambda : mean_squared_error(df=self.sf_df,y_true_col_names=self.true_cn, y_pred_col_names=self.pred_cn))
        detailed_matrix_dict[mean_absolute_error.__name__] = try_or(lambda : mean_absolute_error(df=self.sf_df,y_true_col_names=self.true_cn, y_pred_col_names=self.pred_cn))
        detailed_matrix_dict[r2_score.__name__] = try_or(lambda : r2_score(df=self.sf_df,y_true_col_name=self.true_cn, y_pred_col_name=self.pred_cn))
        detailed_matrix_dict["Root Mean Square Error"] =  math.sqrt(detailed_matrix_dict[mean_squared_error.__name__])
        detailed_dict = {"tag": "detailed_matrix", "model_metric_value": detailed_matrix_dict}
        update_progress(self.progress_counter / self.progress_base_value)
        self.progress_counter += 1
        return detailed_dict


class Classification:

    def __init__(self, model_obj, sf_df,true_cn,pred_cn,pred_proba_cn):
        """
        Constructor to initialize the model object
        """
        self.sf_df = sf_df 
        self.true_cn = true_cn
        self.pred_cn = pred_cn 
        self.pred_proba_cn = pred_proba_cn
        self.progress_base_value = 3
        self.progress_counter = 1
        self.model = model_obj

    def get_metrics(self):
        """
        Method to get metrics  
        """ 
        all_summary = [
                self.confusion_metrics(),
                # self.decision_tree(),
                self.detailed_matrix(),
                # self.cal_roc_auc(),
                self.cal_feature_importance()
        ]
        return all_summary

    def cal_feature_importance(self):
        """
        Method to calculate variable importance

        Returns:
            String
        """
        try:
            imp_list = []
            sklearn_model = self.model.to_sklearn()
            for index , value in zip(sklearn_model.feature_names_in_,sklearn_model.feature_importances_.tolist()):
                imp_list.append({"column_name": index, "importance": value})
        except Exception:
            imp_list = None
        feature_importance_dict = {
            "tag": "feature_importance",
            "model_metric_value": imp_list,
        }
        update_progress(self.progress_counter / self.progress_base_value)
        self.progress_counter += 1
        return feature_importance_dict

    def confusion_metrics(self):
        """
        Method to return confusion matrix string

        Returns:
            String
        """
        try:
            dlist = []
            conf_matrix = confusion_matrix(df=self.sf_df, y_true_col_name=self.true_cn, y_pred_col_name=self.pred_cn)
            conf_list = conf_matrix.tolist()
            for idx, item in enumerate(conf_list):
                for index, val in enumerate(item):
                    d = {
                        "column_1_counter": idx,
                        "column_2_counter": index,
                        "prediction": val,
                        "column_1": idx,
                        "column_2": index,
                    }
                    dlist.append(d.copy())
        except Exception as ex:
            dlist = None
        conf_dict = {"tag": "confusion_matrix", "model_metric_value": dlist}
        update_progress(self.progress_counter / self.progress_base_value)
        self.progress_counter += 1
        return conf_dict

    def detailed_matrix(self):
        """
        Method to calculate detailed matrix parameters

        Returns:
            String
        """
        temp_model = self.model.to_sklearn() if str(type(self.model)).find("snowflake") > 0 else self.model
        average='weighted' if temp_model.n_classes_ > 2 else 'binary'
        detailed_matrix_dict = {}
        detailed_matrix_dict[accuracy_score.__name__] = try_or(lambda : accuracy_score(df=self.sf_df,y_true_col_names=self.true_cn, y_pred_col_names=self.pred_cn))
        detailed_matrix_dict[precision_score.__name__] = try_or(lambda : precision_score(df=self.sf_df,y_true_col_names=self.true_cn, y_pred_col_names=self.pred_cn,average=average))
        detailed_matrix_dict[recall_score.__name__] = try_or(lambda : recall_score(df=self.sf_df,y_true_col_names=self.true_cn, y_pred_col_names=self.pred_cn,average=average))
        detailed_matrix_dict[f1_score.__name__] = try_or(lambda : f1_score(df=self.sf_df,y_true_col_names=self.true_cn, y_pred_col_names=self.pred_cn,average=average))
        detailed_matrix_dict[log_loss.__name__] = try_or(lambda : log_loss(df=self.sf_df,y_true_col_names=self.true_cn, y_pred_col_names=self.pred_cn))
        # detailed_matrix_dict[roc_auc_score.__name__]  =  try_or(lambda: roc_auc_score(df=self.sf_df,y_true_col_names=self.true_cn, y_score_col_names=self.pred_cn))
        detailed_dict = {"tag": "detailed_matrix", "model_metric_value": detailed_matrix_dict}
        update_progress(self.progress_counter / self.progress_base_value)
        self.progress_counter += 1
        return detailed_dict

    def cal_roc_auc(self):
        """
        Method to calculate roc auc curve parameters

        Returns:
            String
        """
        try:
            roc_auc = roc_auc_score(df=self.sf_df, y_true_col_names=self.true_cn, y_score_col_names=self.pred_cn ,average="macro")
            fpr, tpr, thresholds = roc_curve(df=sf_df,y_true_col_name=self.true_cn,y_score_col_name=self.pred_cn)
            fpr = fpr.tolist()
            tpr = tpr.tolist()
            roc_auc_value = {"fpr": fpr, "tpr": tpr, "data": roc_auc}
        except Exception as ex:
            roc_auc_value = None
        roc_auc_dict = {"tag": "roc_auc", "model_metric_value": roc_auc_value}
        update_progress(self.progress_counter / self.progress_base_value)
        self.progress_counter += 1
        return roc_auc_dict