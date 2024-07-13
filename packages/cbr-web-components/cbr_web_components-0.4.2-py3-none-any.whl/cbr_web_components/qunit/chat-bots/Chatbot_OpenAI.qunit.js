import Chatbot_OpenAI   from '../../js/chat-bots/Chatbot_OpenAI.mjs'
import Web_Component    from '../../js/core/Web_Component.mjs'
import WebC__Target_Div from "../../js/utils/WebC__Target_Div.mjs";

QUnit.module('Chatbot_OpenAI', function(hooks) {

    let chatbot_openai
    let target_div

    hooks.before(async (assert) => {
        chatbot_openai = Chatbot_OpenAI
        target_div = WebC__Target_Div.add_to_body().build({width: "50%"})        
        target_div.append_child(chatbot_openai)
        //await webc_events_viewer.load_datatables_css() 
    });
 

    QUnit.test('constructor', (assert) => {
        assert.ok(true)
        //assert.ok(chatbot_openai instanceof Chatbot_OpenAI)
        //assert.ok(Chatbot_OpenAI.prototype instanceof Web_Component);
    })
})