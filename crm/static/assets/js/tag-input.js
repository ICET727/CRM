class RblTagInput extends HTMLElement {
    createdCallback() {
        this.createShadowRoot();
        this.tags = [];
    }
    attachedCallback() {
        this.shadowRoot.innerHTML = ``;
    }
}
document.registerElement("rbl-tag-input", RblTagInput);

let allowDelete = false;
this.shadowRoot.querySelector('#tag-input').addEventListener("keydown", (event) => {
    let tag = this.shadowRoot.querySelector('#tag-input').value;
    if (event.keyCode === 13) {
        this.addTag(tag);
    } else if (event.keyCode === 188) {
        event.preventDefault();
        this.addTag(tag);
    } else if (event.keyCode === 8 && tag.length === 0) {
        if (allowDelete) {
            this.deleteTag(this.tags.length - 1);
            allowDelete = false;
        } else {
            allowDelete = true;
        }
    }
});

var $element = this.shadowRoot.querySelector('[data-index="' + this.tags.indexOf(tag) + '"]');
$element.className = ($element.className + " duplicate");
setTimeout(function() {
    $element.className = $element.className.replace("duplicate", "");
}, 500);

var $element = document.querySelector("#tagElement");
$element.clear();

var $element = document.querySelector("#tagElement");
console.log($element.value); //Web Components, JavaScript, AngularJS