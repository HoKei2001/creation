def resume_generator_tool(shared_variables, instruction: str):
    '''Generate mock resume/candidate data based on instruction.
    
    This function creates mock data for job platforms (Boss直聘/猎聘/LinkedIn)
    based on the provided instruction. It returns the data in a standardized format.
    
    Args:
        shared_variables: Dictionary containing shared variables including the agent
        instruction: String containing keywords and parameters for data generation
        
    Returns:
        JSON response with generated data
    '''
    agent = shared_variables['agent']
    
    return strict_json(f'''Generate mock resume data based on ```{instruction}```.
The instruction should contain job keywords and optional parameters.

You can choose one of the following data generation modules:
1. BOSS直聘 (boss_search) - Chinese recruitment platform
2. 猎聘网 (liepin_search) - Chinese executive recruitment platform  
3. LinkedIn (linkedin_search) - International professional network

For example:
- "Generate 5 BOSS直聘 candidates for Python developer"
- "Find 10 LinkedIn profiles for marketing specialists"
- "Get 20 猎聘 resumes for Java engineers with 5+ years experience"

You are able to use the following Equipped Functions:```
{agent.list_functions(
fn_list = [agent.function_map[function_name] for function_name in agent.function_map if function_name not in ['use_llm', 'end_task']])}
```The result will contain candidates with appropriate fields based on the platform.
Use "###GeneratedData###" for json output field''',
                      '',
                      output_format = {'GeneratedData': 'type: array'},
                      llm = agent.llm)