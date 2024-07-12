// import antlr from "antlr4";
import { CharStream, CommonTokenStream, CommonToken } from 'antlr4ng';
import { tags, Tag } from '@lezer/highlight';
import { StreamLanguage, StringStream } from '@codemirror/language';
import { jsoniqLexer } from '../grammar/jsoniqLexer.js';

interface IToken {
  tokenName: string;
  text: string;
  type: number;
  startIndex: number;
  stopIndex: number;
}

interface ITokenizerState {
  tokenValueClassFromPreviousTokenContext: string;
  hasTokenValueClassFromPreviousToken: boolean;
}

class Tokenizer {
  private tokens;

  constructor(text: string) {
    this.tokens = this.getTokensForText(text);
  }

  private getTokensForText(text: string) {
    const chars = CharStream.fromString(text);
    const lexer = new jsoniqLexer(chars);
    const tokensStream = new CommonTokenStream(lexer);
    tokensStream.fill();
    return this.convertCommonTokensToTokens((tokensStream as any).tokens);
  }

  private convertCommonTokensToTokens(tokens: CommonToken[]): IToken[] {
    return tokens.map(token => {
      return {
        tokenName: this.getTokenNameByTokenValue(token.type),
        text: token.text || '',
        type: token.type,
        startIndex: token.start,
        stopIndex: token.stop
      };
    });
  }

  private getTokenNameByTokenValue(tokenValue: number): string {
    for (const tokenName in jsoniqLexer) {
      if (((jsoniqLexer as any)[tokenName] as number) === tokenValue) {
        return tokenName;
      }
    }
    return '';
  }

  public findCurrentToken(streamPos: number): IToken {
    return this.tokens.filter(t => t.startIndex >= streamPos)[0];
  }
}

export class TokenToCodeMirrorStyleConverter {
  private currToken;
  private stream;
  private state;

  constructor(currToken: IToken, stream: StringStream, state: ITokenizerState) {
    this.currToken = currToken;
    this.stream = stream;
    this.state = state;
  }

  private getStyleNameByTag(tag: Tag): string {
    for (const t in tags) {
      if ((tags as any)[t] === tag) {
        return t;
      }
    }
    return '';
  }

  public convertTokenToCodeMirrorStyle() {
    if (
      this.state.hasTokenValueClassFromPreviousToken &&
      this.stream.match(this.currToken.text)
    ) {
      // Some previous context set the current token's class
      this.state.hasTokenValueClassFromPreviousToken = false;
      return this.state.tokenValueClassFromPreviousTokenContext;
    } else {
      return this.convertCurrentTokenToCodeMirrorStyle();
    }
  }

  private convertCurrentTokenToCodeMirrorStyle() {
    if (
      this.currToken.type !== jsoniqLexer.EOF &&
      this.stream.match(this.currToken.text)
    ) {
      let valueClass;
      switch (this.currToken.type) {
        case jsoniqLexer.T__1:
          // $ symbol
          valueClass = this.getStyleNameByTag(tags.variableName);
          break;
        case jsoniqLexer.NCName:
          valueClass = this.getStyleNameByTag(tags.variableName);
          break;
        case jsoniqLexer.Kversion:
        case jsoniqLexer.Kcontext:
        case jsoniqLexer.Ktype:
        case jsoniqLexer.Kfor:
        case jsoniqLexer.Ktypeswitch:
        case jsoniqLexer.Kswitch:
        case jsoniqLexer.Kif:
        case jsoniqLexer.Kthen:
        case jsoniqLexer.Kelse:
        case jsoniqLexer.Ktry:
        case jsoniqLexer.Kcatch:
        case jsoniqLexer.Kwhere:
        case jsoniqLexer.Kgroup:
        case jsoniqLexer.Kby:
        case jsoniqLexer.Korder:
        case jsoniqLexer.Kas:
        case jsoniqLexer.Kat:
        case jsoniqLexer.Kin:
        case jsoniqLexer.Kdeclare:
        case jsoniqLexer.Kimport:
        case jsoniqLexer.Kreplace:
        case jsoniqLexer.Kvalue:
        case jsoniqLexer.Kof:
        case jsoniqLexer.Krename:
        case jsoniqLexer.Kinsert:
        case jsoniqLexer.Kdelete:
        case jsoniqLexer.Kcopy:
        case jsoniqLexer.Kappend:
        case jsoniqLexer.Kwith:
        case jsoniqLexer.Kmodify:
        case jsoniqLexer.Kinto:
        case jsoniqLexer.Kbreak:
        case jsoniqLexer.Kloop:
        case jsoniqLexer.Kcontinue:
        case jsoniqLexer.Kexit:
        case jsoniqLexer.Kreturning:
        case jsoniqLexer.Kwhile:
        case jsoniqLexer.Kannotate:
        case jsoniqLexer.Kvalidate:
        case jsoniqLexer.Kcastable:
        case jsoniqLexer.Kcast:
        case jsoniqLexer.Ktreat:
        case jsoniqLexer.Kis:
        case jsoniqLexer.Kstatically:
        case jsoniqLexer.Kinstance:
        case jsoniqLexer.Kto:
        case jsoniqLexer.Kcollation:
        case jsoniqLexer.Ksatisfies:
        case jsoniqLexer.Kstable:
        case jsoniqLexer.Kempty:
        case jsoniqLexer.Kallowing:
        case jsoniqLexer.Kreturn:
        case jsoniqLexer.Kleast:
        case jsoniqLexer.Kgreatest:
        case jsoniqLexer.Ksome:
        case jsoniqLexer.Kevery:
        case jsoniqLexer.Kascending:
        case jsoniqLexer.Kdescending:
        case jsoniqLexer.Kordering:
        case jsoniqLexer.Kordered:
        case jsoniqLexer.Kcase:
        case jsoniqLexer.Kdefault:
        case jsoniqLexer.Kunordered:
        case jsoniqLexer.Keq:
        case jsoniqLexer.Kne:
        case jsoniqLexer.Klt:
        case jsoniqLexer.Kle:
        case jsoniqLexer.Kgt:
        case jsoniqLexer.Kge:
        case jsoniqLexer.Kand:
        case jsoniqLexer.Kor:
        case jsoniqLexer.Knot:
        case jsoniqLexer.Kcontext_dollars:
        case jsoniqLexer.Ktrue:
        case jsoniqLexer.Kfalse:
        case jsoniqLexer.NullLiteral:
          valueClass = this.getStyleNameByTag(tags.keyword);
          break;
        case jsoniqLexer.XQComment:
          valueClass = this.getStyleNameByTag(tags.comment);
          break;
        case jsoniqLexer.STRING:
          valueClass = this.getStyleNameByTag(tags.string);
          break;
        case jsoniqLexer.Literal:
        case jsoniqLexer.NumericLiteral:
        case jsoniqLexer.DoubleLiteral:
        case jsoniqLexer.IntegerLiteral:
        case jsoniqLexer.DecimalLiteral:
          valueClass = this.getStyleNameByTag(tags.number);
          break;
        case jsoniqLexer.T__33:
        case jsoniqLexer.T__34:
          // [] brackets
          valueClass = this.getStyleNameByTag(tags.squareBracket);
          break;
        case jsoniqLexer.T__2:
        case jsoniqLexer.T__3:
          // {} braces
          valueClass = this.getStyleNameByTag(tags.brace);
          break;
        case jsoniqLexer.T__4:
        case jsoniqLexer.T__5:
          // () parenthesis
          valueClass = this.getStyleNameByTag(tags.paren);
          break;
        case jsoniqLexer.T__27:
        case jsoniqLexer.T__28:
        case jsoniqLexer.T__6:
        case jsoniqLexer.T__29:
        case jsoniqLexer.T__31:
        case jsoniqLexer.Kassign:
          // +, -, *, div, mod, :=
          valueClass = this.getStyleNameByTag(tags.operator);
          break;
        case jsoniqLexer.T__9:
        case jsoniqLexer.T__0:
          // ",",  ";"
          valueClass = this.getStyleNameByTag(tags.separator);
          break;
        case jsoniqLexer.T__35:
          // "."
          valueClass = this.getStyleNameByTag(tags.derefOperator);
          this.state.tokenValueClassFromPreviousTokenContext =
            this.getStyleNameByTag(tags.propertyName);
          this.state.hasTokenValueClassFromPreviousToken = true;
          break;
        case jsoniqLexer.Kfunction:
        case jsoniqLexer.Kvariable:
        case jsoniqLexer.Klet:
          valueClass = this.getStyleNameByTag(tags.keyword);
          break;
        case jsoniqLexer.Knamespace:
        case jsoniqLexer.Kexternal:
          valueClass = this.getStyleNameByTag(tags.namespace);
          break;
        case jsoniqLexer.Kmodule:
          valueClass = this.getStyleNameByTag(tags.moduleKeyword);
          break;
        case jsoniqLexer.T__8:
          // "%"
          valueClass = this.getStyleNameByTag(tags.annotation);
          break;
        default:
          valueClass = this.getStyleNameByTag(tags.variableName);
          break;
      }
      return valueClass;
    } else {
      this.stream.next();
      return null;
    }
  }
}

export const jsoniqLanguageDefinition = StreamLanguage.define({
  startState: _ => {
    return {
      tokenValueClassFromPreviousTokenContext: '',
      hasTokenValueClassFromPreviousToken: false
    };
  },
  token: (stream, state: ITokenizerState) => {
    const tokenizier = new Tokenizer(stream.string);
    const tokenConverter = new TokenToCodeMirrorStyleConverter(
      tokenizier.findCurrentToken(stream.pos),
      stream,
      state
    );
    return tokenConverter.convertTokenToCodeMirrorStyle();
  },
  copyState(state) {
    return {
      tokenValueClassFromPreviousTokenContext:
        state.tokenValueClassFromPreviousTokenContext,
      hasTokenValueClassFromPreviousToken:
        state.hasTokenValueClassFromPreviousToken
    };
  }
});
