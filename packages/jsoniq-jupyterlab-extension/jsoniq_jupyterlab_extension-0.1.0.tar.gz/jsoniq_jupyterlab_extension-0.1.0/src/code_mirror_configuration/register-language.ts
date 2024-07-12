import { LanguageSupport } from '@codemirror/language';
import { IEditorLanguageRegistry } from '@jupyterlab/codemirror';
import { jsoniqLanguageDefinition } from './tokenizer.js';

export class RegisterJSONiqInCodeMirror {
  private codeMirrorRecognizedLanguages;
  constructor(codeMirrorRecognizedLanguages: IEditorLanguageRegistry) {
    this.codeMirrorRecognizedLanguages = codeMirrorRecognizedLanguages;
  }

  public registerJSONiqLanguage() {
    this.codeMirrorRecognizedLanguages.addLanguage({
      name: 'jsoniq',
      displayName: 'JSONiq',
      mime: ['application/jsoniq', 'text/jsoniq', 'text/x-jsoniq'],
      extensions: ['.jq'],
      support: new LanguageSupport(jsoniqLanguageDefinition) as any
    });
  }
}
