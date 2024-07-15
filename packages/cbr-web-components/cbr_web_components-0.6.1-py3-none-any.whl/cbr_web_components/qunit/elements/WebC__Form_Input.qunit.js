import WebC__Target_Div from "../../js/utils/WebC__Target_Div.mjs";
import Web_Component    from '../../js/core/Web_Component.mjs'
import WebC__Form_Input from "../../js/elements/WebC__Form_Input.mjs";

QUnit.module('WebC__Form_Input', function(hooks) {

    let webc_form_input
    let target_div
    let target_div_setup

    hooks.before(async (assert) => {
        target_div_setup = { right:"50px", top:"250px", width: "500px", height:"100px"}
        target_div       = WebC__Target_Div.add_to_body().build(target_div_setup)
        webc_form_input   = target_div.append_child(WebC__Form_Input)

        //target_div.shadow_root().querySelector('.target_div').style.border = '0px'
        //window.target_div = target_div
    });


    QUnit.test('build', (assert) => {
        const expected_html = `\
<div id="form_input">
    <textarea id="text_area"></textarea>
</div>
`
        //console.log(webc_form_input.inner_html())
        assert.equal(webc_form_input.shadow_root().innerHTML, webc_form_input.inner_html())
        assert.equal(webc_form_input.inner_html() , expected_html)
        assert.ok(1)
    })

    QUnit.test('constructor', (assert) => {
        assert.ok(WebC__Form_Input.prototype instanceof Web_Component, 'WebC__Save_Chat.prototype is an instance of Web_Component');
        assert.ok       (webc_form_input instanceof Web_Component     , 'webc_save_chat is an instance of Web_Component')
        assert.deepEqual(webc_form_input.channels, [ 'Web_Component' ], 'webc_save_chat.channels == [ "Web_Component" ]')
    })


})