import { ReactWidget } from '@jupyterlab/ui-components';

import React from 'react';

/**
 * React component for a counter.
 *
 * @returns The React component
 */
// const CounterComponent = (props:any): JSX.Element => {
//   // const [counter, setCounter] = useState(0);

//   return (
//     <div>
//       <p>点击跳转（数据集.csv）</p>
//       <button
//         onClick={(): void => {
//           props.execute('docmanager:open', { path: '数据集.csv' });
//         }}
//       >
//         数据集
//       </button>
//     </div>
//   );
// };

/**
 * A Counter Lumino Widget that wraps a CounterComponent.
 */
export class ExampleWidget extends ReactWidget {
  /**
   * Constructs a new CounterWidget.
   */
  props: any;
  constructor(props:any) {
    super();
    this.props = props
    this.addClass('jp-react-widget');
  }

  render(): JSX.Element {
    return <div>
    <p>点击跳转（数据集.csv）</p>
    <button
      onClick={(): void => {
        this.props.execute('docmanager:open', { path: '数据集.csv' });
      }}
    >
      数据集
    </button>
  </div>;
  }
}
