## Query multiple LLMs 

At the same time



{{chatbot   name             = "Main Chat bot" 
            initial_message  = "Hi, Ask a question here and see the answer in multiple LLMs" 
            initial_prompt   = "Hi"
            edit_mode        = "false"
            platform         = "Groq (Free)"
            provider         = "Meta"
            model            = "llama3-70b-8192"
            channel          = "root-llm"
}}
<div class="row">
    <div class="col-4">
        {{chatbot   name               = "in Meta (Spanish)"  
                    system_prompt      = "Only reply in Spanish"
                    show_sent_messages = "false"
                    edit_mode          = "false" 
                    platform           = "Groq (Free)"
                    provider           = "Meta"
                    model              = "llama3-70b-8192"
                    channel            = "shared-llm-es" 
        }}
    </div>
    <div class="col-4">
        {{chatbot   name               = "in Meta (Portuguese)"  
                    system_prompt      = "Only reply in Portuguese"
                    show_sent_messages = "false"
                    edit_mode          = "false" 
                    platform           = "Groq (Free)"
                    provider           = "Meta"
                    model              = "llama3-70b-8192"
                    channel            = "shared-llm-pt" 
        }}
    </div>
    <div class="col-4">
        {{chatbot   name               = "in Meta (French)"  
                    system_prompt      = "Only reply in French"
                    show_sent_messages = "false"
                    edit_mode          = "false" 
                    platform           = "Groq (Free)"
                    provider           = "Meta"
                    model              = "llama3-70b-8192"
                    channel            = "shared-llm-fr" 
        }}
    </div>
</div>  

<div class="row">
    <div class="col-4">
        {{chatbot   name               = "in Meta (Japanese)"  
                    system_prompt      = "Only reply in Japanese"
                    show_sent_messages = "false"
                    edit_mode          = "false" 
                    platform           = "Groq (Free)"
                    provider           = "Meta"
                    model              = "llama3-70b-8192"
                    channel            = "shared-llm-jp" 
        }}
    </div>
    <div class="col-4">
        {{chatbot   name               = "in Meta (Emojis)"  
                    system_prompt      = "Only reply in Emojis"
                    show_sent_messages = "false"
                    edit_mode          = "false" 
                    platform           = "Groq (Free)"
                    provider           = "Meta"
                    model              = "llama3-70b-8192"
                    channel            = "shared-llm-emj" 
        }}
    </div>
    <div class="col-4">
        {{chatbot   name               = "in Meta (klingon)"  
                    system_prompt      = "Only reply in klingon"
                    show_sent_messages = "false"
                    edit_mode          = "false" 
                    platform           = "Groq (Free)"
                    provider           = "Meta"
                    model              = "llama3-70b-8192"
                    channel            = "shared-llm-kl" 
        }}
    </div>
</div>  

<script type="module" src="/web_components/js/chat-bots/Chatbot_OpenAI.mjs"></script>
<script src="/assets/plugins/marked/marked.min.js"></script>
