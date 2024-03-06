import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  
  configuration: any;
  presetsArray: any;
  optionsArray: any;

  title = 'angular-app';

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.http.get<any>('http://localhost:5000/').subscribe(data => {
      this.configuration = data.configuration;
      this.presetsArray = data.presetsArray;
      this.optionsArray = data.optionsArray;
    });
  }

}
