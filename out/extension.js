"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = activate;
exports.deactivate = deactivate;
const vscode = __importStar(require("vscode"));
const axios_1 = __importDefault(require("axios"));
function activate(context) {
    const translateCommand = vscode.commands.registerCommand('translate-this-text->_<', async () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showInformationMessage('Откройте текстовый файл/среду');
            return;
        }
        const selection = editor.selection;
        const textToTranslate = editor.document.getText(selection).trim();
        if (textToTranslate === '') {
            vscode.window.showInformationMessage('Выделите текст для перевода');
            return;
        }
        const targetLanguage = await vscode.window.showQuickPick(['en', 'ru'], {
            placeHolder: 'Выберите язык для перевода',
        });
        if (!targetLanguage) {
            return;
        }
        const sourceLanguage = targetLanguage === 'en' ? 'ru' : 'en';
        try {
            const response = await axios_1.default.get('https://api.mymemory.translated.net/get', {
                params: {
                    q: textToTranslate,
                    langpair: `${sourceLanguage}|${targetLanguage}`,
                },
            });
            const translatedText = response.data.responseData.translatedText; // Получение переведенного текста
            await editor.edit(editBuilder => {
                editBuilder.replace(selection, translatedText);
            });
            vscode.window.showInformationMessage('Перевод успешен!');
        }
        catch (err) {
            const errorMessage = err instanceof Error ? err.message : JSON.stringify(err);
            console.log('Текст для перевода:', textToTranslate);
            console.log('Исходный язык:', sourceLanguage);
            console.log('Целевой язык:', targetLanguage);
            console.log('Ошибка:', errorMessage);
            vscode.window.showErrorMessage(`Ошибка при переводе: ${errorMessage}`);
        }
    });
    context.subscriptions.push(translateCommand);
}
function deactivate() { }
//# sourceMappingURL=extension.js.map