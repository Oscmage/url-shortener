import { FC } from "react";
import { GET_ALIAS_URL } from "./Constants";

interface ResultProps {
  success: boolean | null;
  error: string | null;
  url: string | null;
  alias: string | null;
}

const ResultDialog: FC<ResultProps> = ({ success, error, url, alias }) => {
  if (success == null) {
    return <></>;
  }
  if (success && url) {
    return (
      <div className="success-dialog">
        <div>
          <label>Success!</label>
        </div>
        <div>
          <label>
            Url: <a href={GET_ALIAS_URL + alias}>{GET_ALIAS_URL + alias}</a>
          </label>
        </div>
      </div>
    );
  } else {
    return (
      <div className="success-dialog">
        <div>
          <label>Failure :(</label>
        </div>
        <div>
          <label>Error: {error}</label>
        </div>
      </div>
    );
  }
};

export default ResultDialog;
