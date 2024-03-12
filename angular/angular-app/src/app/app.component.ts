import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Subscription } from 'rxjs';
import { AppService } from './services/app.service';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  
  configuration: any;
  presetsArray: any;
  optionsArray: any;
  subscriber: Subscription;

  title = 'angular-app';

  constructor(private appService: AppService) {
    this.subscriber = appService.messages.subscribe(data => {
      data = JSON.parse(data)
      console.log(data);
      this.configuration = data.configuration;
      this.presetsArray = data.presetsArray;
      this.optionsArray = data.optionsArray;
    })
  }

  // ngOnInit(): void {
  //   console.log("Going into ngOnInit now");
  // }

}
