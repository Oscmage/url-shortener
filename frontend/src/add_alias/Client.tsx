import axios from "axios";
import { CREATE_ALIAS_URL } from "./Constants";

export type CreateAlias = (
  url: string,
  alias: string
) => Promise<CreateAliasResponse>;

export interface CreateAliasResponse {
  success: boolean;
  error: string | null;
  url: string | null;
  alias: string | null;
}

export const addAlias: CreateAlias = async (
  url: string,
  alias: string
): Promise<CreateAliasResponse> => {
  return await axios
    .post(CREATE_ALIAS_URL, { url: url, alias: alias })
    .then((res) => {
      return {
        success: true,
        error: null,
        alias: res.data.alias,
        url: res.data.url,
      };
    })
    .catch((err) => {
      return {
        success: false,
        error: err.response.data.detail,
        alias: null,
        url: null,
      };
    });
};
