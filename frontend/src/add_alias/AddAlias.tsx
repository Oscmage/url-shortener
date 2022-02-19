import React from 'react';
import ErrorDialog from './ErrorDialog';
import InputField from './Input';
//import "./CreateMonitoring.css";

interface AddAliasState {
    formDisabled: boolean;
    alias: string;
    aliasError: string;
    url: string;
    urlError: string;
    success: boolean;
}

const initialState = {
    formDisabled: false,
    alias: "",
    aliasError: "",
    url: "",
    urlError: "",
    success: false,
};

export class AddAlias extends React.Component<{},AddAliasState> {
  constructor(props: any) {
    super(props);
    this.state = initialState
  }

  render() {
      const errorExists = this.state.urlError !== "" || this.state.aliasError !== ""
    return (
        <fieldset disabled={this.state.formDisabled}>
            <form onSubmit={this.handleSubmit}>
                <div className="alias-wrapper">
                    {<InputField placedholder="alias" value={this.state.alias} onChange={this.handleInputChangeAlias} errorMessage={this.state.aliasError}/>}
                </div>
                <div className="alias-wrapper">
                    {<InputField placedholder="https://google.com" value={this.state.url} onChange={this.handleInputChangeUrl} errorMessage={this.state.urlError}/>}
                </div>
                <button disabled={errorExists ? true: false}>Submit</button>
                {this.state.success ? "success" : null}
            </form>
      </fieldset>
    );
  }

  handleInputChangeUrl = (event: any) => {
    const target = event.target;
    const value = target.value;
    const urlError = this.validateUrl(value)

    this.setState({
      url: value,
      urlError,
    });
  };


  handleInputChangeAlias = (event: any) => {
    const target = event.target;
    const value = target.value;
    const aliasError = this.validateAlias(value)
    
    this.setState({
      alias: value,
      aliasError,
    });
  };

  validateAlias = (alias: string) => {
    var regexp = /^[a-zA-Z0-9-_]+$/;
    if (alias === "") {
        return ""
    }

    if (alias.search(regexp) === -1) { 
        return "Only alphanumeric symbols, dash or underscore are allowed";
    }
    else { 
        return ""
    }
  }

  validateUrl = (url: string) => {
    let res
    if (url === "") {
        return ""
    }
    try {
        res = new URL(url);
        return ""
      } catch (_) {
        return "Not a valid url";  
      }
  }



  handleSubmit = async (event: any) => {
    event.preventDefault();
    this.setState({
        formDisabled: true
    })
    console.log(this.state)

    /*const error: string | null = await this.props.create(
      this.state.name,
      this.state.url
    );
    
    if (error !== null) {
      alert("Received error: " + error);
    } else {
      
    }
    */
    //this.setState(initialState);
  };
}