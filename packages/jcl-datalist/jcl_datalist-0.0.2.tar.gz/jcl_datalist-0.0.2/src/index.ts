 import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';
import { MainAreaWidget } from '@jupyterlab/apputils';
import { ICommandPalette } from '@jupyterlab/apputils';
import { ExampleWidget  } from './widget'
import { Widget } from '@lumino/widgets';
// import { MySidebarItem} from './widget'
class Button extends Widget {  
  constructor(options: { label: string, onClick?: () => void }) {  
    super();  
    this.addClass('lm-MenuBar'); // 添加一个 CSS 类以便样式化  
  
    // 创建按钮的 DOM 元素  
    const buttonNode = document.createElement('div'); 
    buttonNode.textContent = options.label; 
    buttonNode.classList.add('lm-MenuBar-item')
    buttonNode.onclick = options.onClick;  
  
    // 将按钮的 DOM 元素添加到 widget 的节点中  
    this.node.appendChild(buttonNode);  
  }  
}  
  
// // ... 然后你可以在你的插件中使用 MyButton ...
class MySidebarItem extends Widget {  
  constructor(app: JupyterFrontEnd) {  
    super();  
    this.id = 'jcldata-dashboard-launcher';  
    this.title.label = 'Open Settings';  
    this.title.closable = true;  
    const handleClick = () => {  
      console.log('Button was clicked!');
      app.commands.execute('widgets:open-tab');    
    }; 
    // 创建按钮并添加到侧边栏项中  
    const button = new Button({ label: '数据集',onClick: handleClick });  
    this.node.appendChild(button.node);  
  }  
} 
// // ... 然后你可以在你的插件中使用 MyButton ...
class MySidebarItem2 extends Widget {  
  constructor(app: JupyterFrontEnd) {  
    super();  
    this.id = 'jcldata-dashboard-launcher2';  
    this.title.label = 'Open Settings';  
    this.title.closable = true;  
    const handleClick2 = () => {    
      app.commands.execute('help:open', {
        url: 'http://localhost:8888/doc',
       // url: 'http://aistrategy.jincelue.net:184/ydjzb/diplonema?active=2',
        text: '比赛'
      })
    }; 
    // 创建按钮并添加到侧边栏项中  
    const button2 = new Button({ label: '比赛',onClick: handleClick2 });
    this.node.appendChild(button2.node); 
  }  
} 
/**
 * Activate the widgets example extension.
 */
const extension: JupyterFrontEndPlugin<void> = {
  id: 'jcl-labextension:plugin',
  description: '数据集',
  autoStart: true,
  requires: [ICommandPalette],
  activate: (app: JupyterFrontEnd, palette: ICommandPalette) => {
    const { commands, shell } = app;
    const command = 'widgets:open-tab';

    commands.addCommand(command, {
      label: 'Open a Tab Widget',
      caption: 'Open the Widgets Example Tab',
      execute: () => {
        const content = new ExampleWidget(commands);
        const widget = new MainAreaWidget<ExampleWidget>({ content });
        widget.id = 'jcldata-dashboard-launcher';
        widget.title.label = '数据集';
        widget.title.closable = true;
        shell.add(widget, 'main');
      }
    });

    const widget = new MySidebarItem(app);  
    const widget2 = new MySidebarItem2(app);
    // 将侧边栏项添加到左侧侧边栏  
    app.shell.add(widget, 'top', { rank: 200 });
    app.shell.add(widget2, 'top', { rank: 201 });
    if(palette) {
      palette.addItem({ command, category: 'Extension Examples' });
    }
  }
};

export default extension;
