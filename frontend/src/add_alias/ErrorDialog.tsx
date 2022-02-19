

import React, { FC } from 'react';

interface ErrorProps {
  msg: string;
}

const ErrorDialog: FC<ErrorProps> = ({ msg }) => {
  return (
    <>
        { msg ? <label>{msg}</label> : null}
    </>
  );
};

export default ErrorDialog;