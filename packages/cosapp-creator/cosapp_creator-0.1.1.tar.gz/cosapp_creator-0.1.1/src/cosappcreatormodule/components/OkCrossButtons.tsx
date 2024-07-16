import React from 'react';

interface IProps {
  closePopUp: () => void;
}

/** Validation buttons for a form in a pop up */
export function OkCrossButtons({ closePopUp }: IProps) {
  return (
    <div className="controls">
      <button type="button" onClick={closePopUp}>
        &#128473;
      </button>
      <button type="submit">Ok</button>
    </div>
  );
}

/** Close and Ok buttons for a pop up */
type IPropsForm = IProps & { handleOk: () => void };

export function OkCrossForm({ closePopUp, handleOk }: IPropsForm) {
  const handleSubmit = (e: React.FormEvent) => {
    handleOk();
    e.preventDefault();
  };

  return (
    <form onSubmit={handleSubmit} className="formPopUp">
      <OkCrossButtons closePopUp={closePopUp} />
    </form>
  );
}
