import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map, Observable, Observer } from 'rxjs';
import { environment } from '../../environments/environment';
import { AnonymousSubject, Subject } from 'rxjs/internal/Subject';

const SOCKET_URL = environment.websocket_endpoint;

@Injectable({
  providedIn: 'root'
})
export class AppService {

  private subject: any;
  public messages: Subject<any>;

  constructor() {
    this.messages = <Subject<any>>this.connect(SOCKET_URL).pipe(
      map(
        (response: any): any => {
          let data = JSON.parse(response.data)
          return data;
        }
      )
    )
  }

  public connect(url: string): AnonymousSubject<any> {
    if (!this.subject) {
      this.subject = this.create(url);
    }
    return this.subject
  }

  public create(url: string): AnonymousSubject<any> {
    let ws = new WebSocket(url);
    let observable = new Observable((obs: Observer<any>) => {
      ws.onmessage = obs.next.bind(obs);
      ws.onerror = obs.error.bind(obs);
      ws.onclose = obs.complete.bind(obs);
      return ws.close.bind(ws);
    });
    let observer = {
      error: (error: ErrorEvent) => null,
      complete: () => null,
      next: (data: Object) => {
        if (ws.readyState === WebSocket.OPEN) {
          ws.send(JSON.stringify(data));
        }
      }
    };
    return new AnonymousSubject<any>(observer, observable)
  }

  // getData(): Observable<any> {
  //   console.log("HELLO");
  //   return this.http.get<any>(this.apiUrl);
  // }
}