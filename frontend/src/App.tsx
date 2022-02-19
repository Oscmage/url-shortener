
import React from 'react';
import { AddAlias } from './add_alias/AddAlias';
import { addAlias, CreateAliasRequest, CreateAliasResponse } from './add_alias/Client';
import ResultDialog from './add_alias/ResultDialog';
import './App.css';

interface AppState {
  success: boolean;
  error: string | null;
  url: string | null;
  alias: string | null;
}

export class App extends React.Component<{}, AppState> {

  constructor(props: any) {
    super(props);
    this.state = {
      success: false,
      error: null,
      url: null,
      alias: null,
    }
  }

  render() {
    console.log(this.addAliasWrapper)
    return (
      <div className="App">
        <header className="App-header">
          <AddAlias create={this.addAliasWrapper}/>
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


addAliasWrapper: CreateAliasRequest["create"] = async (
  url: string,
  alias: string,
): Promise<CreateAliasResponse> => {
  const res: Promise<CreateAliasResponse> = addAlias(url, alias)
  res.then((res) => {
    this.setState({
      success: res.success,
      error: res.error,
      url: res.url,
      alias: res.alias,
    });
  });
  return res;
};

}

export default App;
