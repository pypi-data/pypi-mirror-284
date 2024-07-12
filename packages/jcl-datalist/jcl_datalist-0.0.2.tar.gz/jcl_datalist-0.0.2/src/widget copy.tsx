
import { Widget } from '@lumino/widgets';
import { Message } from '@lumino/messaging';
import * as React from 'react';
// import * as ReactDOM from 'react-dom';


export class ExampleWidget extends Widget {
  props: any;
  private _dashboard: Widget;
  constructor(props: any) {
    super(props);
    this.addClass('jp-example-view');
    this.id = 'jcldata-dashboard-launcher';
    this.title.label = '数据集';
    this.title.closable = true;
    this.props = props
    this._dashboard = new Widget();
    console.log(this._dashboard,'dsjsj')
  }
  handleEvent(event: Event): void {
    switch (event.type) {
      case 'pointerenter':
        this._onMouseEnter(event);
        
        break;
      case 'pointerleave':
        this._onMouseLeave(event);
        break;
    }
  }
  protected onAfterAttach(msg: any): void {
    this.node.addEventListener('pointerenter', this);
    this.node.addEventListener('pointerleave', this);
    // This event will call a specific function when occuring
    this.node.addEventListener('click', this._onEventClick.bind(this));
  }

  /**
   * Callback when the widget is removed from the DOM
   *
   * This is the recommended place to stop listening for DOM events
   */
  protected onBeforeDetach(msg: Message): void {
    this.node.removeEventListener('pointerenter', this);
    this.node.removeEventListener('pointerleave', this);
    this.node.removeEventListener('click', this._onEventClick.bind(this));
  }

  /**
   * Callback on click on the widget
   */
  private _onEventClick(event: Event): void {
    this.props.execute('docmanager:open', { path: '数据集.csv' })
    // window.alert('You clicked on the widget');
  }

  /**
   * Callback on pointer entering the widget
   */
  private _onMouseEnter(event: Event): void {
   // this.node.style['backgroundColor'] = 'orange';
  }

  /**
   * Callback on pointer leaving the widget
   */
  private _onMouseLeave(event: Event): void {
    // this.node.style['backgroundColor'] = 'aliceblue';
  }
  // render(): JSX.Element {
  //   return <div>23333</div>
  //   ;
  // }

  render(): JSX.Element | null {
    return  <div className="cesss">
        222
    </div>
  }
  // protected onUpdateRequest(): void {
  //   console.log('jddjj222')
  //   ReactDOM.render(
  //     <div className="cesss">
  //       222
  //       </div>
  //     ,
  //     this._dashboard.node
  //   )
  // }
}