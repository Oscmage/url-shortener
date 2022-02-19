import React from "react";
import { Form } from "./add_alias/Form";
import { addAlias, CreateAlias, CreateAliasResponse } from "./add_alias/Client";
import ResultDialog from "./add_alias/ResultDialog";
import "./App.css";

const initialAppState = {
  success: null,
  error: null,
  url: null,
  alias: null,
  formDisabled: false,
};

interface AppState {
  success: boolean | null;
  error: string | null;
  url: string | null;
  alias: string | null;
  formDisabled: boolean;
}

export class App extends React.Component<{}, AppState> {
  constructor(props: any) {
    super(props);
    this.state = initialAppState;
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <Form
            create={this.addAliasWrapper}
            disabled={this.state.formDisabled}
          />
          <ResultDialog
            success={this.state.success}
            error={this.state.error}
            url={this.state.url}
            alias={this.state.alias}
          />
        </header>
      </div>
    );
  }

  addAliasWrapper: CreateAlias = async (
    url: string,
    alias: string
  ): Promise<CreateAliasResponse> => {
    // Disable form when making a call
    this.setState({
      formDisabled: true,
    });

    const res: Promise<CreateAliasResponse> = addAlias(url, alias);
    res.then((res) => {
      this.setState({
        success: res.success,
        error: res.error,
        url: res.url,
        alias: res.alias,
      });
    });

    // Make sure we reset and allow the possibility to add more aliases
    setTimeout(() => {
      this.setState(initialAppState);
    }, 5000);
    return res;
  };
}

export default App;
