import React, { useEffect, useRef, useState } from 'react';
import { sysNameCrit } from '../tools/widgetParams';

interface CustomInputProps {
  placeholder: string;
  parentState: string;
  setParentState: (val: string, options?: any) => void;
  setShow: (val: boolean, options?: any) => void;
}

/** Input that disappear when it is submitted */
function CustomInput(props: CustomInputProps) {
  const [value, setValue] = useState(props.parentState);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => inputRef.current?.select(), []);

  const inputSubmit = () => {
    const { current } = inputRef;
    if (current && current.reportValidity()) {
      props.setParentState(value);
      props.setShow(false);
    }
  };

  const handleKeyUp = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      inputSubmit();
    }
    e.preventDefault();
  };

  return (
    <input
      ref={inputRef}
      type="text"
      className="nodrag defaultTextInput center"
      placeholder={props.placeholder}
      {...sysNameCrit}
      required
      value={value}
      onChange={e => setValue(e.target.value)}
      onKeyUp={handleKeyUp}
      onBlur={inputSubmit}
    />
  );
}

export default CustomInput;
