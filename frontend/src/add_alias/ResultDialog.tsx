

import React, { FC } from 'react';

interface ResultProps {
  success: boolean;
  error: string | null;
  url: string | null;
  alias: string | null;
}

const ResultDialog: FC<ResultProps> = ({ success, error, url, alias }) => {
  if (success) {
    return (
      <div>
          <label>Success!</label>
          <label>Alias: {alias}</label>
          <label>Url: {url}</label>
      </div>
    )
  } else {
    return (
      <div>
          <label>Failure :(</label>
          <label>Error: {error}</label>
      </div>
    )
  }
};

export default ResultDialog;