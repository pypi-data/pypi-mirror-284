import { RegExpForeignCodeExtractor } from '@jupyter-lsp/jupyterlab-lsp';
import { ILSPCodeExtractorsManager } from '@jupyterlab/lsp';

export class JSONiqExtractor {
  private extractorManager: any;
  constructor(extractorManager: ILSPCodeExtractorsManager) {
    this.extractorManager = extractorManager;
  }

  public registerExtractor() {
    const jsoniqExtractor = new RegExpForeignCodeExtractor({
      language: 'jsoniq',
      pattern: '^%%(jsoniq)( .*?)?\n([^]*)',
      foreignCaptureGroups: [3],
      isStandalone: true,
      fileExtension: 'jq'
    });
    this.extractorManager.register(jsoniqExtractor, 'python');
  }
}
