import { FC } from "react";
import ErrorDialog from "./ErrorDialog";

interface InputProps {
  placedholder: string;
  value: string;
  onChange: any; // TODO: fix type
  errorMessage: string;
}

const InputField: FC<InputProps> = ({
  placedholder,
  value,
  onChange,
  errorMessage,
}) => {
  return (
    <div className="input-wrapper">
      <input
        placeholder={placedholder}
        value={value}
        onChange={onChange}
      ></input>
      {<ErrorDialog msg={errorMessage} />}
    </div>
  );
};

export default InputField;
