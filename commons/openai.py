from langchain.chat_models import PromptLayerChatOpenAI, ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings

INVALID_RESPONSE_VALUES = ["N/A", "", " ", "-", "--", "---", "----", ":--", ":---", ":-", "unknown"]

chat_gpt35_turbo_prompt_layer = PromptLayerChatOpenAI(model_name="gpt-3.5-turbo",
                                                      frequency_penalty=0.1,
                                                      temperature=0,
                                                      return_pl_id=True,
                                                      pl_tags=["chatgpt"],
                                                      )

chat_gpt35_turbo_ft_re_prompt_layer = PromptLayerChatOpenAI(
    model_name="ft:gpt-3.5-turbo-0613:national-institute-for-materials-science::8QSHUZ7C",
    frequency_penalty=0.1,
    temperature=0,
    return_pl_id=True,
    pl_tags=["chatgpt", "finetune", "re"],
)

chat_gpt35_turbo_ft_re_shuffled_prompt_layer = PromptLayerChatOpenAI(
    model_name="ft:gpt-3.5-turbo-0613:national-institute-for-materials-science::8feTZsMW",
    frequency_penalty=0.1,
    temperature=0,
    return_pl_id=True,
    pl_tags=["chatgpt", "finetune", "re"],
)

chat_gpt35_turbo_ft_re_shuffled_augmented_prompt_layer = PromptLayerChatOpenAI(
    model_name="ft:gpt-3.5-turbo-0613:national-institute-for-materials-science::8fKTJ18v",
    frequency_penalty=0.1,
    temperature=0,
    return_pl_id=True,
    pl_tags=["chatgpt", "finetune", "re"],
)

chat_gpt35_turbo_ft_ner_materials_prompt_layer = PromptLayerChatOpenAI(
    model_name="ft:gpt-3.5-turbo-0613:national-institute-for-materials-science::8QrWl2Ca",
    frequency_penalty=0.1,
    temperature=0,
    return_pl_id=True,
    pl_tags=["chatgpt", "finetune", "ner", "materials"],
)

chat_gpt35_turbo_ft_ner_quantities_prompt_layer = PromptLayerChatOpenAI(
    model_name="ft:gpt-3.5-turbo-0613:national-institute-for-materials-science::8SJzMGs2",
    frequency_penalty=0.1,
    temperature=0,
    return_pl_id=True,
    pl_tags=["chatgpt", "finetune", "ner", "quantities"],
)

chat_gpt35_turbo = ChatOpenAI(model_name="gpt-3.5-turbo",
                              frequency_penalty=0.1,
                              temperature=0)

chat_gpt4_prompt_layer = PromptLayerChatOpenAI(model_name="gpt-4",
                                               frequency_penalty=0.1,
                                               temperature=0,
                                               return_pl_id=True,
                                               pl_tags=["gpt4"],
                                               )

chat_gpt4_turbo_prompt_layer = PromptLayerChatOpenAI(model_name="gpt-4-1106-preview",
                                                     frequency_penalty=0.1,
                                                     temperature=0,
                                                     return_pl_id=True,
                                                     pl_tags=["gpt4"],
                                                     )
gpt4_turbo = ChatOpenAI(model_name="gpt-4-1106-preview",
                        frequency_penalty=0.1,
                        temperature=0
                        )

chat_gpt4 = PromptLayerChatOpenAI(model_name="gpt-4",
                                  frequency_penalty=0.1,
                                  temperature=0,
                                  return_pl_id=True,
                                  pl_tags=["gpt4"],
                                  )

embeddings_open = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

CHATS = {
    'chatgpt': chat_gpt35_turbo_prompt_layer,
    'chatgpt-ft-re': chat_gpt35_turbo_ft_re_prompt_layer,
    'chatgpt-ft_shuffled-re': chat_gpt35_turbo_ft_re_shuffled_prompt_layer,
    'chatgpt-ft_shuffled-augmented-re': chat_gpt35_turbo_ft_re_shuffled_augmented_prompt_layer,
    'chatgpt-ft-ner-materials': chat_gpt35_turbo_ft_ner_materials_prompt_layer,
    'chatgpt-ft-ner-quantities': chat_gpt35_turbo_ft_ner_quantities_prompt_layer,
    'gpt4': chat_gpt4_prompt_layer,
    'gpt4-turbo': chat_gpt4_turbo_prompt_layer
}
