from langchain.prompts import PromptTemplate  # type: ignore

def get_prompt_login(contexts: str, history: str, latest_chat: str, query: str) -> str:
    """
    The function returns formatted prompt to get answer to the user query.
    :param contexts: str
    :param history: str
    :param latest_chat: str
    :param query: str
    :return: str
    """
    prompt_template = PromptTemplate(
        input_variables=["contexts", "history", "latest_chat", "query"],
        template="""
        You are an expert in login systems, providing ***accurate and detailed*** answers based on the available information.

        Strictly follow these guidelines:
        - Use **Context (Knowledge Base)** as the primary source to answer **User Query**.
        - If the **User Query** cannot be answered using **Context**, refer to **History Summary**.
        - If the answer is still unclear, consider **Latest Chat** for additional context.
        - Do not use **History Summary** or **Latest Chat** if **Context** provides a complete answer. (!!!THIS IS IMPORTANT!!!)

        - provide a detailed and accurate asnwer based on above guidelines.
        - Do not generate any additional explanation.

        **Context (Knowledge Base - Primary Source):**
        {contexts}

        **History Summary (Secondary Source - Past Conversations Overview):**
        {history}

        **Latest Chat (Tertiary Source - Most Recent User Interaction):**
        {latest_chat}

        **User Query (Answer This Based on the Given Sources):**
        {query} 
        """
    )
    
    formatted_prompt = prompt_template.format(
        contexts=contexts, history=history, latest_chat=latest_chat, query=query
    )
    return formatted_prompt


# def get_prompt_enrollment(contexts: str, history: str, latest_chat: str, query: str) -> str:
#     """
#     Generates a structured prompt to answer a user's query regarding insurance enrollment.

#     :param contexts: str - Primary knowledge base information.
#     :param history: str - Summary of past interactions.
#     :param latest_chat: str - Most recent user interaction.
#     :param query: str - User's current query.
#     :return: str - Formatted prompt for generating a response.
#     """
    
#     prompt_template = PromptTemplate(
#         input_variables=["contexts", "history", "latest_chat", "query"],
#         template=
#         """
#             ### SYSTEM MESSAGE  
#             You are an expert in **insurance enrollment** chatbot that provides **accurate, clear, and direct** responses to help user.

#             ### GUIDELINES  
#             1. Use **only the information provided** to answer the user's query.  
#             2. **DO NOT** say "Based on the Context" or "mention in context" reference the sources directly.  
#             3. **Rephrase and integrate** the information naturally—avoid copying text verbatim.  
#             4. If the query **cannot** be answered with certainty, say so rather than making assumptions.  
#             5. **DO NOT** use any special formatting (e.g., bold, italics, hyperlinks) from the source.  


#             ---

#             ### BACKGROUND INFORMATION (Use This to Answer the Query) 
#             {contexts}  

#             ---

#             ### LATEST USER INTERACTION  
#             {latest_chat}   

#             ---

#             ### USER QUERY  (Provide a natural, well-structured response here.)
#             {query}  
#         """
#     )
    
#     return prompt_template.format(
#         contexts=contexts, history=history, latest_chat=latest_chat, query=query
#     )

def get_prompt_enrollment(contexts: str, history: str, latest_chat: str, query: str) -> str:
    """
    Generates a structured prompt to ensure the model provides a natural, context-aware response 
    without directly referencing source material.
    
    :param contexts: str - Primary knowledge base information.
    :param history: str - Summary of past interactions.
    :param latest_chat: str - Most recent user interaction.
    :param query: str - User's current query.
    :return: str - Formatted prompt for generating a response.
    """
    
    prompt_template = PromptTemplate(
        input_variables=["contexts", "history", "latest_chat", "query"],
        template=
        
        """
            ### SYSTEM MESSAGE  
            You are an **insurance enrollment expert**, and your task is to **answer the user's query** in a **clear and natural manner**. 

            **IMPORTANT:**
            - **Do NOT** reference the source text (Context, History, or Latest Chat) directly in your response.
            - **Do NOT quote or copy-paste** content from the provided information.
            - **DO NOT say "Based on the Context" or similar phrases**.
            - Integrate the relevant information into a **natural, fluent response** without explicitly calling out where it came from.
            - If the query **cannot be answered with the available information**, **honestly state** that the answer is unclear.
            - Ensure that your response **does not repeat verbatim** the language in the source material.

            ### BACKGROUND INFORMATION (Use this to answer the query):
            {contexts}

            ### LATEST USER INTERACTION:
            {latest_chat}

            ### HISTORY SUMMARY (Use this if needed for additional context):
            {history}

            ### USER QUERY:
            {query}

            ### RESPONSE:
            (Provide a concise, clear response. Integrate information without repeating source text or referring to the context explicitly.)
        """
    )

    return prompt_template.format(
        contexts=contexts, history=history, latest_chat=latest_chat, query=query
    )


def get_validation_prompt(response: str, query: str) -> str:
    prompt_template = PromptTemplate(
        input_variables=["response", "query"],
        template=
        """  
        You are an AI assistant validating an insurance response that exactly follows the below instructions.

        - Check if the response is extremely irrelavant to the user query. Return **"I don't have enough information on that, Please contact the office or provide more details."**.
        - If the response is relevant, return the response provided itself.
        - Don't generate any additional explanations.
        
        **User Question:**  
        {query}  

        **Response Provided:**  
        {response}  
        """
    )

    formatted_prompt = prompt_template.format(query=query, response=response)
    print(f"Formatted Prompt: {formatted_prompt}")
    return prompt_template.format(response=response, query=query)


def get_query_category(query: str) -> str:
    prompt_template = PromptTemplate(
        input_variables=["query"],
        template=
        """
        You are an AI assistant categorizing user queries related to login and user accounts.
        
        - If the query is related to login, username, password, or account access, return **"login"**.
        - For all other queries, return **"enrollment"**.
        - Don't generate any additional explanations.

        **User Query:**  
        {query}  
        """
    )
    
    formatted_prompt = prompt_template.format(query=query)
    print(f"Formatted Prompt: {formatted_prompt}")
    return prompt_template.format(query=query)

def get_summarize_prompt(data):

    """Takes in conversation history data and returns a formatted prompt."""

    prompt_template = PromptTemplate(
        input_variables=["data"],
        template="""
        You are an AI assistant that **summarizes** the given **conversation data**.
        Optimize the summary so that it provides sufficient context for an LLM about the chat history.
        Limit the summary to 1000 characters to ensure it is concise and informative.
        If **Conversation Data** is **Empty** return "History Empty".

        **Conversation Data:**
        {data}
        """
    )

    formatted_prompt = prompt_template.format(data=data)

    return formatted_prompt