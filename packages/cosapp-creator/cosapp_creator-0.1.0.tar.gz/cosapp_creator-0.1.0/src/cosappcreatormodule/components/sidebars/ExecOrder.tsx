import React, { useState, useRef, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';

import { systemType } from '../../tools/customTypes';
import { getMousePosInWidget } from '../../tools/genericFunctions';

interface SystemListProps {
  systemList: systemType[];
  setSystemList: (val: systemType[], options?: any) => void;
}

interface SysProps {
  index: number;
  name: string;
  dragFrom: number;
  setDragFrom: (val: number, options?: any) => void;
  dragTo: number;
  setDragTo: (val: number, options?: any) => void;
}

function ExecOrderSystem(props: SysProps & SystemListProps) {
  const { index, name, dragFrom, setDragFrom, dragTo, setDragTo, systemList } =
    props;
  const sysDivRef = useRef<HTMLDivElement>(null);
  const [ellisped, setEllipsed] = useState(false);
  const [show, setShow] = useState(false);
  const [pos, setPos] = useState({ top: 0, left: 0 });

  const reinitialiseIndex = () => {
    setDragFrom(-1);
    setDragTo(-1);
  };

  /** Set `dragFrom` to the index of the dragged system */
  const handleDragStart = (event: React.DragEvent) => {
    setDragFrom(index);
    event.dataTransfer.setData('text/html', '');
  };

  /** Set `systemList` with the right order */
  const handleDrop = () => {
    if (dragFrom !== -1 && dragTo !== -1) {
      const itemDragged = systemList[dragFrom];

      let newSystemList = [...systemList];
      newSystemList.splice(dragFrom, 1);
      newSystemList = [
        ...newSystemList.slice(0, dragTo),
        itemDragged,
        ...newSystemList.slice(dragTo)
      ];

      props.setSystemList(newSystemList);
      reinitialiseIndex();
    }
  };

  /** Set `dragTo` to the index of the system under the drag */
  const handleDragOver = (event: React.DragEvent) => {
    event.preventDefault();

    if (dragFrom !== -1) {
      const draggedToIndex = index;
      if (draggedToIndex !== dragTo) {
        setDragTo(draggedToIndex);
      }
    }
  };

  const getCssClass = () => {
    let result = 'hiddenOverflow flowNode system';
    if (index === dragFrom) {
      result += ' selectedSys';
    } else if (index === dragTo) {
      result += ' dropArea';
    }
    return result;
  };

  useEffect(() => {
    if (!sysDivRef.current) throw new Error('Element does not exists.');
    const { scrollWidth, offsetWidth } = sysDivRef.current;
    setEllipsed(offsetWidth - scrollWidth < 6); // 6 for borders
  }, []);

  /** Move the hover with the mouse. */
  const handleMouseMove = (event: React.MouseEvent) => {
    if (!show) {
      setShow(true);
    }
    const { top, left } = getMousePosInWidget(event);
    // 15 and 8 are so that the hover won't be right under the mouse
    setPos({ top: top + 50, left: left + 8 });
  };

  return (
    <div>
      <div
        ref={sysDivRef}
        draggable
        onDragStart={handleDragStart}
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        onDragLeave={() => setDragTo(-1)}
        className={getCssClass()}
        onMouseEnter={() => setShow(true)}
        onMouseMove={handleMouseMove}
        onMouseLeave={() => setShow(false)}
      >
        {name}
      </div>
      {ellisped && show ? (
        <div className="hover" style={pos}>
          <ReactMarkdown>{`\`${name}\``}</ReactMarkdown>
        </div>
      ) : (
        ''
      )}
    </div>
  );
}

type APILoopsCall = { checkLoops: (allPbl?: boolean) => Promise<void> };
function CheckMenu(props: APILoopsCall) {
  return (
    <div className="checkMenu">
      <div className="title">Checks</div>
      <button type="button" onClick={() => props.checkLoops()}>
        Check loops
      </button>
      <button type="button" onClick={() => props.checkLoops(true)}>
        Mathematical problem
      </button>
    </div>
  );
}

function ExecOrder(props: SystemListProps & APILoopsCall) {
  const { systemList } = props;
  const [dragFrom, setDragFrom] = useState(-1);
  const [dragTo, setDragTo] = useState(-1);

  return (
    <div className="sidebar execOrderSidebar">
      <div className="title">Execution order</div>
      <div className="orderList">
        {props.systemList.length > 0 ? (
          props.systemList.map(system => (
            <ExecOrderSystem
              key={system.name}
              name={system.name}
              index={systemList.indexOf(system)}
              dragFrom={dragFrom}
              setDragFrom={setDragFrom}
              dragTo={dragTo}
              setDragTo={setDragTo}
              systemList={systemList}
              setSystemList={props.setSystemList}
            />
          ))
        ) : (
          <div style={{ textAlign: 'justify' }}>Empty</div>
        )}
      </div>
      <CheckMenu checkLoops={props.checkLoops} />
    </div>
  );
}

export default ExecOrder;
