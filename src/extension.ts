import * as vscode from 'vscode';
import axios from 'axios';

export function activate(context: vscode.ExtensionContext) {
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
            const response = await axios.get('https://api.mymemory.translated.net/get', {
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
        } catch (err) {
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

export function deactivate() {}
