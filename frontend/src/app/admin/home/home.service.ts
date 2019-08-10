import { Injectable } from '@angular/core';
import { Routes, Route } from '@angular/router';
import { HomeComponent } from './home.component';

@Injectable({
  providedIn: 'root'
})
export class HomeService {

  /**
  * Creates routes using the shell component and authentication.
  * @param routes The routes to add.
  */
 static childRoutes(routes: Routes): Route {
   return {
     path: 'home',
     component: HomeComponent,
     children: routes,
     data: { reuse: true }
   }
 }
}
