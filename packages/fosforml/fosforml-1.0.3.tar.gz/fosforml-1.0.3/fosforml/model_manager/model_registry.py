from snowflake.ml.registry import Registry
from .snowflakesession import snowflakesession as SnowflakeSession
from .utilities import DatasetManager, Metadata
from fosforml.utils import get_headers
from fosforml.constants import NotebooksAPI
from datetime import datetime
import json,requests
import pandas as pd
from fosforml.constants import ModelConstants

class ModelRegistry:
    def __init__(self,session):
        self.session_instance = SnowflakeSession()
        self.snowflake_session = session
        self.model_registry = Registry(session=self.snowflake_session, 
                                       database_name=self.session_instance.connection_params[0]["connectionDetails"]['defaultDb'],
                                       schema_name=self.session_instance.connection_params[0]["connectionDetails"]['defaultSchema']
                                       )
        self.models_info = self.model_registry.show_models()

    def register_model(self,
                       model,
                       score,
                       model_name,
                       description,
                       conda_dependencies,
                       model_flavour,
                       model_type,
                       sf_input_dataframe,
                       x_train,
                       y_train,
                       x_test,
                       y_test,
                       y_pred,
                       prob,
                       python_version,
                       source,
                       metadata
                       ):
        
        if score :
            return False, "score fuction not supported, implementation is in progress ..."
        
        metrics_errors,metrics = self.get_model_metrics(
                                        source=source,
                                        model=model,
                                        session=self.snowflake_session,
                                        metadata=metadata,
                                        model_type=model_type,
                                        model_flavour=model_flavour,
                                        x_train=x_train,
                                        y_train=y_train,
                                        x_test=x_test,
                                        y_test=y_test,
                                        y_pred=y_pred,
                                        prob=prob,
                                        sf_input_dataframe=sf_input_dataframe
                                        )
        if metrics_errors:
            return False,metrics

        metrics['python_version'] = python_version
        metrics['conda_dependencies'] = conda_dependencies
        

        model_version = self.get_model_version(self.model_registry,model_name)

        
        ## register model
        try:
            self.model_registry.log_model(
                   model,
                   model_name=model_name,
                   version_name=model_version,
                   comment=description,
                   conda_dependencies=conda_dependencies,
                   metrics=metrics,
                   sample_input_data=sf_input_dataframe if model_flavour.lower() == "snowflake" else x_train,
                   python_version=python_version  
                  )
        except Exception as e:
            return False,f"Failed to register model '{model_name}'. {str(e)}"
        
        ## upload model datasets
        dataset_manager = DatasetManager(model_name=model_name,
                                         version_name=model_version,
                                         session=self.snowflake_session
                                         )
        ds_status,ds_message = dataset_manager.upload_datasets(
                                session=self.snowflake_session,
                                datasets={
                                        "x_train": x_train,
                                        "y_train": y_train,
                                        "x_test": x_test,
                                        "y_test": y_test,
                                        "y_pred": y_pred,
                                        "prob": prob
                                    })

        if not ds_status:
            return False,ds_message

        ## update model metadata
        metadata = Metadata(model_registry=self.model_registry)
        metadata_status,metadata_message = metadata.update_model_registry(
            session=self.snowflake_session,
            model_name=model_name,
            model_description=description,
            model_tags={
                "FLAVOR": model_flavour,
                "MODELTYPE": model_type,
                "CREATEDON" : metrics['created_on']
            }
        )

        if not metadata_status:
            return False,metadata_message
        
        return True,f"Model '{model_name}' registered successfully."

    def update_model_details(self,
                             model_name,
                             comments,
                             model_tags):
        metadata = Metadata(model_registry=self.model_registry)
        return metadata.update_model_registry(
            session=self.snowflake_session,
            model_name=model_name,
            model_description=comments,
            model_tags=model_tags
        )

    def get_model_details(self, model_name):
        pass

    def get_model_version(self, registry, model_name):
        model_info = registry.show_models()[registry.show_models()['name']==model_name.upper()]
        if model_info.empty:
            return "v1"
        model_versions = json.loads(model_info.versions.to_list()[0])
        if not model_versions:
            return "v1"
        else:
            last_version = max(model_versions,key=lambda x: int(x[1:]),default='v0')
            return f"v{int(last_version[1:])+1}"
    
    def get_model_metrics(self,
                          source,
                          model,
                          session,
                          metadata,
                          model_type,
                          model_flavour,
                          x_train=None,
                          y_train=None,
                          x_test=None,
                          y_test=None,
                          y_pred=None,
                          prob=None,
                          sf_input_dataframe=None):
        
        metrics = {}
        dataset_errors,model_dataset_details = self.get_dataset_details(
            model=model,session=session,
            model_flavour=model_flavour,
            x_train=x_train,
            y_train=y_train,
            x_test=x_test,
            y_test=y_test,
            y_pred=y_pred,
            prob=prob,
            sf_input_dataframe=sf_input_dataframe
        )
        if dataset_errors:
            return True, model_dataset_details['message']
        
        metrics['dataset_details'] = model_dataset_details['metadata'] if 'metadata' in model_dataset_details else {}

        buildtime_metrics_errors,buildtime_metrics = self.get_model_performance_metrics(model,
                                                                      model_flavour,
                                                                      model_type,
                                                                      model_dataset_details
                                                                      )
        if buildtime_metrics_errors:
            return True,metrics['message']
        
        metrics['model_metrics'] = buildtime_metrics

        metrics['hyper_parameters'] = self.get_hyper_parameters(model)

        source_errors,source_info = self.get_source_details(source)
        if source_errors:
            return True,source_info['message']

        metrics['created_on'] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  
        metrics['created_by'] = self.session_instance.connection_params[0]["connectionDetails"]['dbUserName']
        metrics['status'] = source_info['status']
        metrics['source'] = source_info['source']
        metrics['Repo_Details'] = source_info['repo_details']
        metrics['metadata'] = metadata if metadata else None

        return False, metrics

    def get_hyper_parameters(self,model):
        try:
            if str(type(model)).find("snowflake") > 0:
                return model.to_sklearn().get_params()
            else:
                return model.get_params()
        except Exception as e:
            return f"Failed to get hyper parameters. {str(e)}"

    def get_model_performance_metrics(self,model,
                                      model_flavour,
                                      model_type,
                                      model_dataset_details
                                      ):
        try:
            sf_true_cn = None ; sf_pred_cn = None ; sf_pred_proba_cn = None

            if model_flavour.lower() == ModelConstants.sklearn_model_flavour and str(type(model)).find(ModelConstants.sklearn_model_flavour) > 0:
                
                for col in model_dataset_details['final_df'].columns:
                    if col[1:-1].lower() == model_dataset_details['metadata']['target_column'].lower():
                        sf_true_cn = col

                    if col[1:-1].lower() == model_dataset_details['metadata']['prediction_column'].lower():
                        sf_pred_cn = col
                        
            else:
                sf_true_cn = model_dataset_details['metadata']['target_column']
                sf_pred_cn = model_dataset_details['metadata']['prediction_column']
                sf_pred_proba_cn = model_dataset_details['metadata']['prob_columns']

            if sf_true_cn is None or sf_pred_cn is None :
                return True, "Failed to set snowflake true and prediction columns"

            if model_type.lower() == "classification":
                from fosforml.model_manager.model_metrics import Classification
                classification_metrics = Classification(
                    model_obj=model, 
                    sf_df=model_dataset_details['final_df'],
                    true_cn=sf_true_cn,
                    pred_cn=sf_pred_cn,
                    pred_proba_cn=sf_pred_proba_cn
                )
                return False, classification_metrics.get_metrics()
            
            if model_type.lower() == "regression":
                from fosforml.model_manager.model_metrics import Regression
                regression_metrics = Regression(
                                                model=model,
                                                sf_df=model_dataset_details['final_df'], 
                                                true_cn=sf_true_cn,
                                                pred_cn=sf_pred_cn,
                                                pred_proba_cn=sf_pred_proba_cn
                                                )
                return False, regression_metrics.get_metrics()
            
            else:
                return True, "Invalid model type, please provide valid model type as classification or regression"
        except Exception as msg:
            print(True, {"message": f"Failed to get model performance metrics. {str(msg)}"})
            raise Exception(f"Failed to get model performance metrics. {msg}")
        
        # dummy_data = [{'tag': 'feature_importance', 'model_metric_value': [{'column_name': 'DEPARTMENT', 'importance': 0.14061672606947828}, {'column_name': 'SATISFACTION_LEVEL', 'importance': 0.1104329386548882}, {'column_name': 'LAST_EVALUATION', 'importance': 0.1350624049528422}, {'column_name': 'NUMBER_PROJECT', 'importance': 0.04248402957988852}, {'column_name': 'AVERAGE_MONTLY_HOURS', 'importance': 0.2118735496815215}, {'column_name': 'TIME_SPEND_COMPANY', 'importance': 0.10658202765565672}, {'column_name': 'WORK_ACCIDENT', 'importance': 0.010641980974635002}, {'column_name': 'LEFT', 'importance': 0.16529938539291036}, {'column_name': 'PROMOTION_LAST_5YEARS', 'importance': 0.0770069570381792}]}, {'tag': 'confusion_matrix', 'model_metric_value': [{'column_1_counter': 0, 'column_2_counter': 0, 'prediction': 1404.0, 'column_1': 0, 'column_2': 0}, {'column_1_counter': 0, 'column_2_counter': 1, 'prediction': 380.0, 'column_1': 0, 'column_2': 1}, {'column_1_counter': 1, 'column_2_counter': 0, 'prediction': 1129.0, 'column_1': 1, 'column_2': 0}, {'column_1_counter': 1, 'column_2_counter': 1, 'prediction': 483.0, 'column_1': 1, 'column_2': 1}]}, {'tag': 'detailed_matrix', 'model_metric_value': {'accuracy_score': 0.555654, 'precision_score': 0.5596755504055619, 'recall_score': 0.29962779156327546, 'f1_score': 0.3903030303030303, 'log_loss': 16.01586365258474, 'roc_auc_score': 0.5433116536291713}}, {'tag': 'roc_auc', 'model_metric_value': {'fpr': [0.0, 0.21300448430493274, 1.0], 'tpr': [0.0, 0.29962779156327546, 1.0], 'data': 0.5433116536291713}}]
        # return "dummy_data"
    
    def get_source_details(self,source):
        source_info = {}
        if source is None or source == "":
            source_info['status'] = "Registered"
            source_info['source'] = "NOTEBOOK"
            source_info['repo_details'] = self.get_repo_details()

        elif source is not None and  source.upper() == "EXPERIMENT":
            source_info['status'] = "Experimented"
            source_info['source'] = "EXPERIMENT"

        elif source is not None and source.upper() == "BYOM":
            source_info['status'] = "Deploying"
            source_info['source'] = "BYOM"
            
        elif source is not None and source.upper() == "NOTEBOOK" :
            source_info['status'] = "Registered"
            source_info['source'] = "NOTEBOOK"
            source_info['repo_details'] = self.get_repo_details()    
        else:
            return True, {"message": f"Invalid source. Please provide valid source as Experiment, BYOM or Notebook."}

        return False,source_info

    def get_repo_details(self):
        try:
            url = NotebooksAPI.notebooks_api_server_url + NotebooksAPI.git_repo
            headers = get_headers()
            response = requests.get(url, headers=headers).json()
            return response
        except Exception as e:
            print(e,"Unable to Fetch Repo Details")
            return ""

    def get_dataset_details(self,model,
            session,
            model_flavour,
            x_train=None,
            y_train=None,
            x_test=None,
            y_test=None,
            y_pred=None,
            prob=None,
            sf_input_dataframe=None):
        dataset_details = {}
        dataset_metadata = {}
        purpose = DatasetManager.get_dataset_purpose

        if model_flavour.lower() == "snowflake" and str(type(model)).find("snowflake") > 0:
            try:
                dataset_metadata['feature_names'] = model.input_cols
                dataset_metadata['target_column'] = model.label_cols
                dataset_metadata['prediction_column'] = model.output_cols
                dataset_metadata['prob_columns'] = None
                dataset_metadata['snowflake_input_dataframe'] = {
                'dataset_type' : 'Table',
                'purpose' : 'Validation',
            }   
                dataset_details['final_df'] = sf_input_dataframe
                
            except Exception as msg:
                return True, {"message": f"Failed to get snowflake dataset details. {str(msg)}"}

        elif model_flavour.lower() == "sklearn" and str(type(model)).find("sklearn") > 0:
            try:
                dataset_metadata['feature_names'] = x_train.columns.to_list()
                dataset_metadata['target_column'] = y_train.squeeze().name if isinstance(y_train,pd.DataFrame) else y_train.name
                dataset_metadata['prediction_column'] = y_pred.squeeze().name if isinstance(y_pred,pd.DataFrame) else y_train.name
                dataset_metadata['prob_columns'] = None if prob is None else prob.columns.to_list() if not prob.empty else None
                
                if x_train is not None:
                    dataset_metadata['x_train'] = {
                        'dataset_type' : 'Table',
                        'purpose' : purpose('x_train'),
                    }
                if y_train is not None:
                    dataset_metadata['y_train'] = {
                        'dataset_type' : 'Table',
                        'purpose' : purpose('y_train'),
                    }
                if x_test is not None:
                    dataset_metadata['x_test'] = {
                        'dataset_type' : 'Table',
                        'purpose' : purpose('x_test'),
                    }
                if y_test is not None:
                    dataset_metadata['y_test'] = {
                        'dataset_type' : 'Table',
                        'purpose' : purpose('y_test'),
                    }
                if y_pred is not None:
                    dataset_metadata['y_pred'] = {
                        'dataset_type' : 'Table',
                        'purpose' : purpose('y_pred'),
                    }
                if prob is not None:
                    dataset_metadata['prob'] = {
                        'dataset_type' : 'Table',
                        'purpose' : purpose('prob'),
                    }
            
                
                no_rows = x_test.shape[0]
                temp_dfs = []
                if x_test is not None:
                    temp_dfs.append(self.get_validation_df(x_test,no_rows))
                if y_pred is not None:
                    temp_dfs.append(self.get_validation_df(y_test,no_rows))
                if prob is not None:
                    temp_dfs.append(self.get_validation_df(prob,no_rows))
                if y_pred is not None:
                    temp_dfs.append(self.get_validation_df(y_pred,no_rows))
                
                final_df = pd.concat(temp_dfs,axis=1)

                schema_names = final_df.columns.to_list()
                dataset_details['final_df'] = session.create_dataframe(final_df,schema=schema_names)

            except Exception as msg:
                return True, {"message": f"Failed to get dataset details. {str(msg)}"}
        
        dataset_details['metadata'] = dataset_metadata
        dataset_details['message'] = "Dataset details fetched successfully."
        
        return False,dataset_details


    def get_validation_df(self,df,no_rows):
        if df is not None and not df.empty:
            if isinstance(df,pd.DataFrame):
                return df.reset_index(drop=True).iloc[:no_rows,:]
            if isinstance(df,pd.Series):
                return df.to_frame().reset_index(drop=True).iloc[:no_rows,:]

