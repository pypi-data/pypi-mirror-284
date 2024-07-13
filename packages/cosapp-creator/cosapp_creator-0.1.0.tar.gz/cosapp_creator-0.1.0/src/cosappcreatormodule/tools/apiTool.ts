import axios, { AxiosInstance, AxiosResponse } from 'axios';

interface IRequestOption {
  method: 'get' | 'post' | 'patch' | 'put' | 'delete';
  url: string;
  params?: any;
  data?: any;
  config?: any;
  headers?: any;
}
export class ApiClient {
  constructor({ baseURL }: { baseURL: string }) {
    this._client = axios.create({ baseURL });
  }

  async sendRequest(options: IRequestOption): Promise<AxiosResponse<any, any>> {
    const { method, url, params, data, config, headers } = options;
    if (url.length === 0) {
      throw new Error('Missing url');
    }
    const axios_headers = { Accept: 'application/json', ...(headers ?? {}) };
    return this._client.request({
      method,
      url,
      params,
      data,
      headers: axios_headers,
      ...(config ?? {})
    });
  }

  update(options: Omit<IRequestOption, 'method'>) {
    return this.sendRequest({
      method: 'put',
      ...options
    });
  }

  private _client: AxiosInstance;
}
