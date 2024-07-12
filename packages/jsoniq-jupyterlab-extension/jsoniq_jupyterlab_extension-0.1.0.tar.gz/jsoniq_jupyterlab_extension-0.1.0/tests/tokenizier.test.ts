import { TokenToCodeMirrorStyleConverter } from '../src/code_mirror_configuration/tokenizer';
import { jsoniqLexer } from '../src/grammar/jsoniqLexer';
import { StringStream } from '@codemirror/language';

function createCurrentToken(
  text: string,
  type: number,
  startIndex: number,
  stopIndex?: number
) {
  return {
    tokenName: 'test',
    text,
    type,
    startIndex,
    stopIndex: stopIndex ? stopIndex : text.length
  };
}

function createState(
  tokenValueClassFromPreviousTokenContext: string,
  hasTokenValueClassFromPreviousToken: boolean
) {
  return {
    tokenValueClassFromPreviousTokenContext,
    hasTokenValueClassFromPreviousToken
  };
}

function getJSONiqLexerType(text: string) {
  switch (text) {
    case 'variable':
      return jsoniqLexer.Kvariable;
    case '$':
      return jsoniqLexer.T__1;
    case 'declare':
      return jsoniqLexer.Kdeclare;
    case '+':
      return jsoniqLexer.T__27;
    case ':=':
      return jsoniqLexer.Kassign;
    case ';':
      return jsoniqLexer.T__0;
    case '.':
      return jsoniqLexer.T__35;
    default:
      if (text.match(/\d+$/)) {
        return jsoniqLexer.NumericLiteral;
      }
      return jsoniqLexer.NCName;
  }
}

function getTokensForText(textLine: string) {
  let currIndex = 0;
  const tokens: any = [];
  textLine.split(' ').forEach(word => {
    if (word.length > 0 && word[0] === '$') {
      // variable
      tokens.push(
        createCurrentToken(
          '$',
          getJSONiqLexerType('$'),
          currIndex,
          currIndex + 1
        )
      );
      currIndex++;
      tokens.push(
        createCurrentToken(
          word.substring(1),
          getJSONiqLexerType(word.substring(1)),
          currIndex,
          currIndex + 1
        )
      );
    } else {
      tokens.push(
        createCurrentToken(
          word,
          getJSONiqLexerType(word),
          currIndex,
          currIndex + word.length
        )
      );
    }
    currIndex += word.length + 1; // +1 for whitespace
  });
  return tokens;
}

describe('tokenizer module single tokens', () => {
  test("checks if keyword 'for' is correctly identified", () => {
    const testTokenState = createCurrentToken('for', jsoniqLexer.Kfor, 0, 3);
    const testState = createState('', false);
    const testStringStream = new StringStream('for', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('keyword');
  });

  test("checks if keyword 'function' is correctly identified", () => {
    const testTokenState = createCurrentToken(
      'function',
      jsoniqLexer.Kfunction,
      0,
      7
    );
    const testState = createState('', false);
    const testStringStream = new StringStream('function', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('keyword');
  });

  test("checks if '$' is correctly identified", () => {
    const testTokenState = createCurrentToken('$', jsoniqLexer.T__1, 0, 1);
    const testState = createState('', false);
    const testStringStream = new StringStream('$', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('variableName');
  });

  test('checks if comments are correctly identified', () => {
    const testTokenState = createCurrentToken(
      '(: simple comment :)',
      jsoniqLexer.XQComment,
      0
    );
    const testState = createState('', false);
    const testStringStream = new StringStream('(: simple comment :)', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('comment');
  });

  test('checks if a string is correctly identified', () => {
    const testTokenState = createCurrentToken(
      'some string',
      jsoniqLexer.STRING,
      0
    );
    const testState = createState('', false);
    const testStringStream = new StringStream('some string', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('string');
  });

  test('checks if a number is correctly identified', () => {
    const testTokenState = createCurrentToken(
      '341',
      jsoniqLexer.NumericLiteral,
      0
    );
    const testState = createState('', false);
    const testStringStream = new StringStream('341', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('number');
  });

  test('checks if a double is correctly identified', () => {
    const testTokenState = createCurrentToken(
      '341.34',
      jsoniqLexer.DoubleLiteral,
      0
    );
    const testState = createState('', false);
    const testStringStream = new StringStream('341.34', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('number');
  });

  test("checks if a '[' is correctly identified", () => {
    const testTokenState = createCurrentToken('[', jsoniqLexer.T__33, 0);
    const testState = createState('', false);
    const testStringStream = new StringStream('[', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('squareBracket');
  });

  test("checks if a '}' is correctly identified", () => {
    const testTokenState = createCurrentToken('{', jsoniqLexer.T__3, 0);
    const testState = createState('', false);
    const testStringStream = new StringStream('{', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('brace');
  });

  test("checks if a '(' is correctly identified", () => {
    const testTokenState = createCurrentToken('(', jsoniqLexer.T__4, 0);
    const testState = createState('', false);
    const testStringStream = new StringStream('(', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('paren');
  });

  test("checks if a '+' is correctly identified", () => {
    const testTokenState = createCurrentToken('+', jsoniqLexer.T__27, 0);
    const testState = createState('', false);
    const testStringStream = new StringStream('+', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('operator');
  });
  test("checks if a '-' is correctly identified", () => {
    const testTokenState = createCurrentToken('-', jsoniqLexer.T__28, 0);
    const testState = createState('', false);
    const testStringStream = new StringStream('-', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('operator');
  });

  test("checks if a '*' is correctly identified", () => {
    const testTokenState = createCurrentToken('*', jsoniqLexer.T__6, 0);
    const testState = createState('', false);
    const testStringStream = new StringStream('*', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('operator');
  });

  test("checks if a 'div' is correctly identified", () => {
    const testTokenState = createCurrentToken('div', jsoniqLexer.T__29, 0);
    const testState = createState('', false);
    const testStringStream = new StringStream('div', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('operator');
  });

  test("checks if a 'mod' is correctly identified", () => {
    const testTokenState = createCurrentToken('mod', jsoniqLexer.T__31, 0);
    const testState = createState('', false);
    const testStringStream = new StringStream('mod', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('operator');
  });

  test("checks if a ':=' is correctly identified", () => {
    const testTokenState = createCurrentToken(':=', jsoniqLexer.Kassign, 0);
    const testState = createState('', false);
    const testStringStream = new StringStream(':=', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('operator');
  });

  test("checks if a 'namespace' is correctly identified", () => {
    const testTokenState = createCurrentToken(
      'namespace',
      jsoniqLexer.Knamespace,
      0
    );
    const testState = createState('', false);
    const testStringStream = new StringStream('namespace', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('namespace');
  });

  test("checks if a 'module' is correctly identified", () => {
    const testTokenState = createCurrentToken('module', jsoniqLexer.Kmodule, 0);
    const testState = createState('', false);
    const testStringStream = new StringStream('module', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('moduleKeyword');
  });

  test("checks if a '%' is correctly identified", () => {
    const testTokenState = createCurrentToken('%', jsoniqLexer.T__8, 0);
    const testState = createState('', false);
    const testStringStream = new StringStream('%', 0, 0);
    const testConverter = new TokenToCodeMirrorStyleConverter(
      testTokenState,
      testStringStream,
      testState
    );
    expect(testConverter.convertTokenToCodeMirrorStyle()).toBe('annotation');
  });
});

describe('tokenizer module multiple tokens', () => {
  test('variable assignment is correctly identified', () => {
    const testLine = 'declare variable $x := $y + 3;';
    const expectedValueClasses = [
      'keyword',
      'keyword',
      'variableName',
      'variableName',
      'operator',
      'variableName',
      'variableName',
      'operator',
      'number',
      'separator'
    ];
    const tokens = getTokensForText(testLine);
    const testState = createState('', false);
    const testStringStream = new StringStream(testLine, 0, 0);
    tokens.forEach((token: any, idx: any) => {
      const testConverter = new TokenToCodeMirrorStyleConverter(
        token,
        testStringStream,
        testState
      );
      const converterResult = testConverter.convertTokenToCodeMirrorStyle();
      if (converterResult === null) {
        testStringStream.next();
      } else {
        expect(converterResult).toBe(expectedValueClasses[idx]);
      }
    });
  });
});

describe('tokenizer module multiple tokens and state', () => {
  test('variable with property access', () => {
    const testLine = '$var_test.attribute.two';
    const expectedValueClasses = [
      'variableName',
      'variableName',
      'derefOperator',
      'propertyName',
      'derefOperator',
      'propertyName'
    ];
    const tokens = getTokensForText(testLine);
    const transitionState = createState('', false);
    const testStringStream = new StringStream(testLine, 0, 0);
    tokens.forEach((token: any, idx: any) => {
      const testConverter = new TokenToCodeMirrorStyleConverter(
        token,
        testStringStream,
        transitionState
      );
      const converterResult = testConverter.convertTokenToCodeMirrorStyle();
      if (converterResult === null) {
        testStringStream.next();
      } else {
        expect(converterResult).toBe(expectedValueClasses[idx]);
      }
    });
  });
});
