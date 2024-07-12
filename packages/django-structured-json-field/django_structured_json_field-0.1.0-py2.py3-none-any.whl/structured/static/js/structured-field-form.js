(function () {
    'use strict';

    function initCallbacks() {
        window.JSONEditor.defaults.callbacks = {
            "select2": {
                "createQueryParams": function (_editor, params) {
                    return {
                      _q: params.term, // search term
                      page: params.page
                    };
                  },
                "processResultData": function (_editor, data, params) {
                    return {
                        results: data.map(item =>  ({id: item.id, text: item.name})),
                        pagination: {
                            more: false
                        }
                    };
                  },
            }
        };
    }

    function patchSelect2Editor() {
        window.JSONEditor.defaults.editors.select2 = class extends window.JSONEditor.defaults.editors.select2 {
            preBuild() {
                if (this.schema.type === "relation") {
                    this.schema.enum = [];
                }
                super.preBuild();
            }

            async fetchDataFromAPI(value) {
                value = Array.isArray(value) ? value.join(",") : value;
                const url = `${this.options.select2.ajax.url}?_q=_pk__in=${value}`;
                return await fetch(url).then(res => res.json()).catch(_ => [])
            }

            forceAddOption(value, text) {
                if (this.enum_values.includes(value)) return
                this.enum_values.push(value);
                this.enum_options.push(value);
                this.enum_display.push(text);
                this.theme.setSelectOptions(this.input, this.enum_options, this.enum_display);
            }

            setValue(value, initial) {
                if (this.schema.type === "relation") {
                    if (this.schema.multiple && Array.isArray(value)) {
                        if (!value.length) return
                        if (value.every(val => !isNaN(val))) {
                            value = value.map(id => ({ id }));
                        }
                        return this.fetchDataFromAPI(value.map(({ id }) => id)).then(data => {
                            data.forEach(({ id, name }) => { this.forceAddOption(this.typecast(id), name); });
                            super.setValue(value.map(({ id }) => this.typecast(id)), initial);
                        })
                    }
                    if (value?.id) {
                        let { id, name } = value;
                        id = this.typecast(id);
                        this.forceAddOption(id, name);
                        return super.setValue(id, initial)
                    }
                    if (value && !this.enum_values.includes(value)) {
                        return this.fetchDataFromAPI(value).then(data => {
                            let { id, name } = data[0] || {};
                            if (!id) return super.setValue(id, initial)
                            id = this.typecast(id);
                            this.forceAddOption(id, name);
                            super.setValue(id, initial);
                        })
                    }
                }
                super.setValue(value, initial);
            }

            typecast(value) {
                if (value && this.schema.type === "relation") {
                    return this.schema.multiple ? parseInt(value) : value
                }
                return super.typecast(value)
            }

            updateValue(value) {
                if (this.schema.type === "relation") {
                    if (this.schema.multiple && Array.isArray(value)) {
                        value = value.map(val => this.innerUpdateCast(val));
                        this.value = value;
                        return value
                    }
                }
                return super.updateValue(value)
            }

            getValue() {
                if (this.schema.type === "relation") {
                    if (!this.dependenciesFulfilled) {
                        return undefined
                    }
                    if (this.schema.multiple) {
                        return this.value?.map(val => this.typecast(val)) || []
                    }
                    return this.typecast(this.value)
                }
                return super.getValue()
            }

            innerUpdateCast(value) {
                let sanitized = this.enum_values[0];
                value = this.typecast(value || '');
                if (!this.enum_values.includes(value)) {
                    if (this.newEnumAllowed) {
                        sanitized = this.addNewOption(value) ? value : sanitized;
                    }
                } else sanitized = value;
                return sanitized
            }

            afterInputReady() {
                super.afterInputReady();
                if (this.schema.type === "relation") {
                    this.newEnumAllowed = true;
                    this.control?.querySelector('.select2-container')?.removeAttribute('style');
                }
            }
        };
        window.JSONEditor.defaults.resolvers.unshift(function (schema) {
            if (schema.type === "relation" && schema.format === "select2") {
                return "select2"
            }
        });
    }

    function renderForm(element) {
        const schema = JSON.parse(element.dataset.schema);
        console.log("🧱 schema", schema);
        JSON.parse(element.dataset.uischema);
        const formData = JSON.parse(element.dataset.formdata);
        console.log("🫐 formData", formData);
        const inputTextArea = document.getElementById(`id_${element.dataset.name}`);
        const editor = new JSONEditor(element, { 
            schema,
            startval: formData,
            max_depth: 10,
            show_errors: 'always',
        });
        editor.on('change', () => {
            inputTextArea.innerHTML = JSON.stringify(editor.getValue());
        });
    }

    document.addEventListener('DOMContentLoaded', () => {
        JSONEditor.defaults.options.theme = 'html';
        JSONEditor.defaults.options.iconlib = 'fontawesome5';
        initCallbacks();
        patchSelect2Editor();
        const elements = document.querySelectorAll('.structured-field-editor');
        for (let i = 0; i < elements.length; i++) {
            renderForm(elements[i]);
        }
    });

})();
//# sourceMappingURL=structured-field-form.js.map
