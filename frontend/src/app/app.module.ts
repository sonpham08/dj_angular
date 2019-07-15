import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { ShowDataComponent } from './show-data/show-data.component';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';

import { AppRoutingModule } from "./app.router";

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { 
  MatButtonModule, 
  MatCardModule, 
  MatMenuModule, 
  MatToolbarModule, 
  MatIconModule, 
  MatSidenavModule, 
  MatListModule,
} from '@angular/material';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { HeaderComponent } from './header/header.component';

// const appRoutes : Routes = [
//   // {
//   //   path: '',
//   //   component: ShowDataComponent,
//   //   pathMatch: 'full'
//   // },
//   {
//     path: 'login',
//     component: LoginComponent
//   },
//   {
//     path: '**',
//     component: PagenotfoundComponent
//   },
// ];

@NgModule({
  declarations: [
    AppComponent,
    ShowDataComponent,
    PagenotfoundComponent,
    LoginComponent,
    HomeComponent,
    HeaderComponent
  ],
  imports: [
    CommonModule,
    HttpModule,
    AppRoutingModule,
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatButtonModule,
    MatMenuModule,
    MatCardModule,
    MatToolbarModule,
    MatIconModule,
    MatSidenavModule,
    MatListModule,
  ],
  exports: [
    MatButtonModule,
    MatMenuModule,
    MatCardModule,
    MatToolbarModule,
    MatIconModule,
    MatSidenavModule,
    MatListModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
