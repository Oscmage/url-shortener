import React from 'react';
import InputField from './Input';
import axios from "axios";
import { CREATE_ALIAS_URL } from './Constants';
//import "./CreateMonitoring.css";

import { CreateAliasRequest, CreateAliasResponse } from './Client';

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

export class AddAlias extends React.Component<CreateAliasRequest, AddAliasState> {
  constructor(props: any) {
    super(props);
    this.state = initialState
  }

  render() {
    const errorExists = this.state.urlError !== "" || this.state.aliasError !== ""
    
    return (
        <div className="form-wrapper">
            <fieldset disabled={this.state.formDisabled}>
                <form onSubmit={this.handleSubmit}>
                    <div className="alias-wrapper">
                        {<InputField placedholder="alias" value={this.state.alias} onChange={this.handleInputChangeAlias} errorMessage={this.state.aliasError}/>}
                    </div>
                    <div className="url-wrapper">
                        {<InputField placedholder="https://google.com" value={this.state.url} onChange={this.handleInputChangeUrl} errorMessage={this.state.urlError}/>}
                    </div>
                    <button disabled={errorExists ? true: false}>Submit</button>
                    {this.state.success ? "success" : null}
                </form>
            </fieldset>
      </div>
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
    });

    const response: CreateAliasResponse = await this.props.create(this.state.url, this.state.alias);
    if (response.success) {
        console.log("Success!")
        console.log(response.alias)
        console.log(response.url)
        this.setState({
            success: true
        })
    } else {
        console.log("Failure!")
    }
    //this.setState(initialState);
  };

  
}