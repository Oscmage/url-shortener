import { FC } from "react";
import "./ErrorDialog.css";

interface ErrorProps {
  msg: string;
}

const ErrorDialog: FC<ErrorProps> = ({ msg }) => {
  if (msg) {
    return (
      <div className="error-dialog">
        <label>{msg}</label>
      </div>
    );
  }
  return null;
};

export default ErrorDialog;
