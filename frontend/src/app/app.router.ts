import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ShowDataComponent } from './show-data/show-data.component';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';
import { LoginComponent } from './login/login.component';
import { HeaderComponent } from './header/header.component';

const appRoutes: Routes = [
    {
        path: "",
        component: ShowDataComponent,
    },
    {
        path: 'header',
        component: HeaderComponent
    }, 
    {
        path: 'login',
        component: LoginComponent
    },
    {
        path:"**",
        component: PagenotfoundComponent,
    }
]

@NgModule({
    imports: [
        RouterModule.forRoot(
            appRoutes
        )
    ],
    exports: [
        RouterModule
    ]
})

export class AppRoutingModule{}