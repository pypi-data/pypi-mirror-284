from .Mapping import table_gen
from .NL2SQL import query_gen
from .PipelineExec import query_exec, display
from .util import num_tokens_from_messages, num_tokens_from_functions
import autopipeline

function_stage = {"table_gen": "Table Generation", "query_gen": "Query Generation", "query_exec": "Query Execution", "display": "Result Evaluation"}
input_var = {"table_gen": ["query", "table", "columns", "desc", "status", "function_chain", "verbose", "client", "udf", "gpt4"], "query_gen": ["query", "tables", "desc", "status", "verbose", "client", "gpt4"], "query_exec": ["db", "code", "status", "verbose"], "display": ["result", "status", "verbose"]}
res_var = {"table_gen": ["table", "columns", "desc", "status", "require_new", "feedback"], "query_gen": ["code", "status"], "query_exec": ["result", "status", "require_new", "feedback"], "display": ["status"]}

def pipeline_gen(query, db, tables, function_chain, desc, verbose, client, udf, gpt4):
    status = []
    value_dict = {"query": query, "tables": tables, "desc": desc, "db": db, "status": status, "function_chain":function_chain, "verbose": verbose, "client": client, "udf": udf, "gpt4": gpt4}
    while 'code generated' not in status:
        tables = value_dict["tables"]
        desc = value_dict["desc"]
        status = value_dict["status"]
        if verbose:
            print("VERBOSE:"+"Current completed stages: ", status)
            print("VERBOSE:"+"Current table descriptions: ", desc)

        # response = pipeline_gpt(query, function_chain, tables, desc, status, verbose, client, gpt4)

        # try:
        #     func = response.function_call
        #     f = func.name
        # except:
        #     feedback = response.content
        #     return True, feedback, None, None
        f = "query_gen"
        
        print("********** Start", function_stage[f])
        input_vars = [value_dict[v] for v in input_var[f]]
        values = globals()[f](*input_vars)

        if "require_new" in res_var[f] and values[-2]:
            return True, values[-1], None, None
        for name, value in zip(res_var[f], values):
            value_dict[name] = value
        if len(status) >= 3 and status[-1] == status[-2] == status[-3]: # keep looping
            return True, values[-1], None, None
        print("********** Complete", function_stage[f])
    return False, "", value_dict["code"], value_dict["db"]