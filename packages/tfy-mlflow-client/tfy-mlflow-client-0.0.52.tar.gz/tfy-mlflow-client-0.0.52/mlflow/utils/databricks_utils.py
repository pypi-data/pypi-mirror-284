import functools
import logging
import os
import subprocess

from mlflow.utils._spark_utils import _get_active_spark_session

_logger = logging.getLogger(__name__)


def _use_repl_context_if_available(name):
    """
    Creates a decorator to insert a short circuit that returns the specified REPL context attribute
    if it's available.

    :param name: Attribute name (e.g. "apiUrl").
    :return: Decorator to insert the short circuit.
    """

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            try:
                from dbruntime.databricks_repl_context import get_context

                context = get_context()
                if context is not None and hasattr(context, name):
                    return getattr(context, name)
            except Exception:
                pass
            return f(*args, **kwargs)

        return wrapper

    return decorator


def _get_dbutils():
    try:
        import IPython

        ip_shell = IPython.get_ipython()
        if ip_shell is None:
            raise _NoDbutilsError
        return ip_shell.ns_table["user_global"]["dbutils"]
    except ImportError:
        raise _NoDbutilsError
    except KeyError:
        raise _NoDbutilsError


class _NoDbutilsError(Exception):
    pass


def _get_java_dbutils():
    dbutils = _get_dbutils()
    return dbutils.notebook.entry_point.getDbutils()


def _get_command_context():
    return _get_java_dbutils().notebook().getContext()


def _get_extra_context(context_key):
    return _get_command_context().extraContext().get(context_key).get()


def _get_context_tag(context_tag_key):
    tag_opt = _get_command_context().tags().get(context_tag_key)
    if tag_opt.isDefined():
        return tag_opt.get()
    else:
        return None


@_use_repl_context_if_available("aclPathOfAclRoot")
def acl_path_of_acl_root():
    try:
        return _get_command_context().aclPathOfAclRoot().get()
    except Exception:
        return _get_extra_context("aclPathOfAclRoot")


def _get_property_from_spark_context(key):
    try:
        from pyspark import TaskContext  # pylint: disable=import-error

        task_context = TaskContext.get()
        if task_context:
            return task_context.getLocalProperty(key)
    except Exception:
        return None


def is_databricks_default_tracking_uri(tracking_uri):
    return tracking_uri.lower().strip() == "databricks"


@_use_repl_context_if_available("isInNotebook")
def is_in_databricks_notebook():
    if _get_property_from_spark_context("spark.databricks.notebook.id") is not None:
        return True
    try:
        return acl_path_of_acl_root().startswith("/workspace")
    except Exception:
        return False


@_use_repl_context_if_available("isInJob")
def is_in_databricks_job():
    try:
        return get_job_id() is not None and get_job_run_id() is not None
    except Exception:
        return False


def is_in_databricks_runtime():
    try:
        # pylint: disable=unused-import,import-error,no-name-in-module,unused-variable
        import pyspark.databricks

        return True
    except ModuleNotFoundError:
        return False


def is_dbfs_fuse_available():
    with open(os.devnull, "w") as devnull_stderr, open(os.devnull, "w") as devnull_stdout:
        try:
            return (
                subprocess.call(
                    ["mountpoint", "/dbfs"], stderr=devnull_stderr, stdout=devnull_stdout
                )
                == 0
            )
        except Exception:
            return False


@_use_repl_context_if_available("isInCluster")
def is_in_cluster():
    try:
        spark_session = _get_active_spark_session()
        return (
            spark_session is not None
            and spark_session.conf.get("spark.databricks.clusterUsageTags.clusterId") is not None
        )
    except Exception:
        return False


@_use_repl_context_if_available("notebookId")
def get_notebook_id():
    """Should only be called if is_in_databricks_notebook is true"""
    notebook_id = _get_property_from_spark_context("spark.databricks.notebook.id")
    if notebook_id is not None:
        return notebook_id
    acl_path = acl_path_of_acl_root()
    if acl_path.startswith("/workspace"):
        return acl_path.split("/")[-1]
    return None


@_use_repl_context_if_available("notebookPath")
def get_notebook_path():
    """Should only be called if is_in_databricks_notebook is true"""
    path = _get_property_from_spark_context("spark.databricks.notebook.path")
    if path is not None:
        return path
    try:
        return _get_command_context().notebookPath().get()
    except Exception:
        return _get_extra_context("notebook_path")


@_use_repl_context_if_available("runtimeVersion")
def get_databricks_runtime():
    if is_in_databricks_runtime():
        spark_session = _get_active_spark_session()
        if spark_session is not None:
            return spark_session.conf.get(
                "spark.databricks.clusterUsageTags.sparkVersion", default=None
            )
    return None


@_use_repl_context_if_available("clusterId")
def get_cluster_id():
    spark_session = _get_active_spark_session()
    if spark_session is None:
        return None
    return spark_session.conf.get("spark.databricks.clusterUsageTags.clusterId")


@_use_repl_context_if_available("jobGroupId")
def get_job_group_id():
    try:
        dbutils = _get_dbutils()
        job_group_id = dbutils.entry_point.getJobGroupId()
        if job_group_id is not None:
            return job_group_id
    except Exception:
        return None


@_use_repl_context_if_available("replId")
def get_repl_id():
    """
    :return: The ID of the current Databricks Python REPL
    """
    # Attempt to fetch the REPL ID from the Python REPL's entrypoint object. This REPL ID
    # is guaranteed to be set upon REPL startup in DBR / MLR 9.0
    try:
        dbutils = _get_dbutils()
        repl_id = dbutils.entry_point.getReplId()
        if repl_id is not None:
            return repl_id
    except Exception:
        pass

    # If the REPL ID entrypoint property is unavailable due to an older runtime version (< 9.0),
    # attempt to fetch the REPL ID from the Spark Context. This property may not be available
    # until several seconds after REPL startup
    try:
        from pyspark import SparkContext

        repl_id = SparkContext.getOrCreate().getLocalProperty("spark.databricks.replId")
        if repl_id is not None:
            return repl_id
    except Exception:
        pass


@_use_repl_context_if_available("jobId")
def get_job_id():
    try:
        return _get_command_context().jobId().get()
    except Exception:
        return _get_context_tag("jobId")


@_use_repl_context_if_available("idInJob")
def get_job_run_id():
    try:
        return _get_command_context().idInJob().get()
    except Exception:
        return _get_context_tag("idInJob")


@_use_repl_context_if_available("jobTaskType")
def get_job_type():
    """Should only be called if is_in_databricks_job is true"""
    try:
        return _get_command_context().jobTaskType().get()
    except Exception:
        return _get_context_tag("jobTaskType")


@_use_repl_context_if_available("commandRunId")
def get_command_run_id():
    try:
        return _get_command_context().commandRunId().get()
    except Exception:
        # Older runtimes may not have the commandRunId available
        return None


@_use_repl_context_if_available("apiUrl")
def get_webapp_url():
    """Should only be called if is_in_databricks_notebook or is_in_databricks_jobs is true"""
    url = _get_property_from_spark_context("spark.databricks.api.url")
    if url is not None:
        return url
    try:
        return _get_command_context().apiUrl().get()
    except Exception:
        return _get_extra_context("api_url")


@_use_repl_context_if_available("workspaceId")
def get_workspace_id():
    try:
        return _get_command_context().workspaceId().get()
    except Exception:
        return _get_context_tag("orgId")


@_use_repl_context_if_available("browserHostName")
def get_browser_hostname():
    try:
        return _get_command_context().browserHostName().get()
    except Exception:
        return _get_context_tag("browserHostName")


def get_workspace_info_from_dbutils():
    dbutils = _get_dbutils()
    if dbutils:
        browser_hostname = get_browser_hostname()
        workspace_host = "https://" + browser_hostname if browser_hostname else get_webapp_url()
        workspace_id = get_workspace_id()
        return workspace_host, workspace_id
    return None, None
