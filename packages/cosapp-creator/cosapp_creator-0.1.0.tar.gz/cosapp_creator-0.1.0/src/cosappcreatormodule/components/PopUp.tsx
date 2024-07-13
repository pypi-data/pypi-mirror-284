import React, {
  ReactNode,
  useCallback,
  useEffect,
  useRef,
  useState
} from 'react';
import { ClientPosition, HTMLPosition } from '../tools/customTypes';
import { getMousePosInWidget } from '../tools/genericFunctions';
import { systemFlowId } from '../tools/widgetParams';

interface IProps {
  children: ReactNode;
  closePopUp: () => void;
  className?: string;
  style?: React.CSSProperties;
}

interface HTMLElementId {
  elementId?: string;
}

/**
 * Check if the mouse is within the boundaries of `div`.
 * @param div HTMLElement
 * @param mousePosition position of the mouse in the appx
 * @returns `true` if the mouse is in `div`, `false` if not
 */
function isMouseInDiv(div: HTMLElement, { clientX, clientY }: ClientPosition) {
  const rect = div.getBoundingClientRect();
  return (
    rect.left < clientX &&
    clientX < rect.right &&
    rect.top < clientY &&
    clientY < rect.bottom
  );
}

/** Base pop up that closes when you click outside of it and
 * inside the element whose id is `elementId`.
 *
 * Without a background,
 * clicks on the background flow will not be taken into account for the closing click.
 */
function PopUp(props: IProps & HTMLElementId) {
  const popUp = useRef(null);
  const { elementId } = props;
  const element = elementId ? document.getElementById(elementId) : document;

  const close = useCallback((e: Event) => {
    if (e instanceof MouseEvent) {
      const { current } = popUp;
      if (current && !isMouseInDiv(current, e)) {
        props.closePopUp();
      }
    } else {
      throw new Error(`This event is not a ${MouseEvent.name}`);
    }
  }, []);

  if (element) element.addEventListener('mouseup', close);

  useEffect(
    () =>
      element ? () => element.removeEventListener('mouseup', close) : () => '',
    []
  );

  return (
    <div
      ref={popUp}
      className={`popUp ${props.className || ''}`}
      style={props.style}
    >
      {props.children}
    </div>
  );
}

/** Pop up centered in `systemFlow`, with a background for `systemFlow`. */
export function FlowCenteredPopUp(props: IProps) {
  return (
    <>
      <div className="popUpBackground" style={{ zIndex: 4 }}>
        <PopUp
          elementId={systemFlowId}
          {...props}
          className={`centerPopUp ${props.className}`}
        />
      </div>
    </>
  );
}

/**
 * Pop up with free position, with a background for `systemFlow`.
 *
 * Closes when you click outside of the pop up and
 * inside the element whose id is `elementId`.
 */
export function FreePopUp(props: IProps & HTMLElementId) {
  return (
    <>
      <div className="popUpBackground" />
      <PopUp {...props} />
    </>
  );
}

export function MousePopUp(
  props: IProps & HTMLElementId & { mousePos: ClientPosition }
) {
  const [position, setPosition] = useState<HTMLPosition | undefined>(undefined);
  const { mousePos: mousePosition } = props;

  useEffect(() => {
    setPosition(getMousePosInWidget(mousePosition));
  }, [mousePosition]);

  return <FreePopUp {...props} style={position} />;
}
