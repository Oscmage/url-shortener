import axios from "axios";
import { CREATE_ALIAS_URL } from "./Constants";

export interface CreateAliasRequest {
    create: (url: string, alias: string) => Promise<CreateAliasResponse>;
}

export interface CreateAliasResponse {
    success: boolean;
    error: string | null;
    url: string | null;
    alias: string | null;
}

export const addAlias: CreateAliasRequest["create"] = async (
    url: string,
    alias: string,
  ): Promise<CreateAliasResponse> => {
    return await axios
      .post(CREATE_ALIAS_URL, { url: url, alias: alias })
      .then((res) => {
        if (res.status === 200) {
            return {
                success: true,
                error: null,
                alias: res.data.alias,
                url: res.data.url,
            }
        } else {
            return {
                success: false,
                error: res.data,
                alias: null,
                url: null,
            }
        }
      })
      .catch((err) => {
        return {
            success: false,
            error: err,
            alias: null,
            url: null,
        };
      });
  };