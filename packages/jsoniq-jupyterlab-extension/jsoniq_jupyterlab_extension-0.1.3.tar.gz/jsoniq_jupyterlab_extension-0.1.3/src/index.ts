import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';
import { ILSPCodeExtractorsManager } from '@jupyterlab/lsp';
import { JSONiqExtractor } from './extractor/extractors.js';
import { IEditorLanguageRegistry } from '@jupyterlab/codemirror';
import { RegisterJSONiqInCodeMirror } from './code_mirror_configuration/register-language.js';

const PLUGIN_ID = 'davidbuzatu-marian/jsoniq-jupyter-plugin:jsoniq';
const plugin: JupyterFrontEndPlugin<void> = {
  id: PLUGIN_ID,
  requires: [ILSPCodeExtractorsManager as any, IEditorLanguageRegistry],
  activate: (
    _app: JupyterFrontEnd,
    extractors: ILSPCodeExtractorsManager,
    codeMirrorRecognizedLanguages: IEditorLanguageRegistry
  ) => {
    const jsoniqExtractor = new JSONiqExtractor(extractors);
    const jsoniqLanguageRegister = new RegisterJSONiqInCodeMirror(
      codeMirrorRecognizedLanguages
    );
    jsoniqExtractor.registerExtractor();
    jsoniqLanguageRegister.registerJSONiqLanguage();
  },
  autoStart: true
};

export default plugin;
