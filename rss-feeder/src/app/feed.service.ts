import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable()
export class FeedService {
  constructor(private http: HttpClient) { }

  getData(url: string) {
    const localAddress = 'localhost:8888/feed?url=' + url;
    console.log('Sending request to: ', localAddress);
    return this.http.get(localAddress);
  }
}
