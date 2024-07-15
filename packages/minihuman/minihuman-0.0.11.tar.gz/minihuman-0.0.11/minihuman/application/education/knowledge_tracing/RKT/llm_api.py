import os, sys, time, json, math 
import numpy as np 
import pandas as pd 

import openai
from openai import OpenAI


def _response_llm_gpt(message_list,openai_api_key,model_name="gpt-3.5-turbo-0125",timeout=120):
    openai.api_key = openai_api_key
    client = OpenAI(api_key = openai.api_key)
    response = ''
    except_waiting_time = 1
    max_waiting_time = 32
    current_sleep_time = 0.5
    
    start_time = time.time()
    while response == '':
        try:
            completion = client.chat.completions.create(
                model=model_name, # gpt-4o, gpt-4
                messages=message_list,
                temperature=0,
                timeout = timeout,
                max_tokens=3000
            )
                
            response = completion.choices[0].message.content
        except Exception as e:
            print(e)
            time.sleep(current_sleep_time)
            if except_waiting_time < max_waiting_time:
                except_waiting_time *= 2
            current_sleep_time = np.random.randint(0, except_waiting_time-1)
    end_time = time.time()   
    print('llm response time: ',end_time-start_time)     
    return response