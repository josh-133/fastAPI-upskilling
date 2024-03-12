import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AppService {
  private apiUrl = 'http://localhost:5000/'; // Update with your FastAPI endpoint

  constructor(private http: HttpClient) { }

  getData(): Observable<any> {
    console.log("HELLO");
    return this.http.get<any>(this.apiUrl);
  }
}