import { NgModule } from '@angular/core';
import { RouterModule, Routes, PreloadAllModules } from '@angular/router';

import { ShowDataComponent } from './show-data/show-data.component';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { HomeComponent } from './admin//home/home.component';
import { ManageProductComponent } from './admin/manage-product/manage-product.component';
import { ManageCategoryComponent } from './admin/manage-category/manage-category.component';
import { HomeService } from './admin/home/home.service';

export const appRoutes: Routes = [
    HomeService.childRoutes([]),
    {
        path: "",
        component: ShowDataComponent,
    },
    {
        path: 'login',
        component: LoginComponent
    },
    {
        path: 'register',
        component: RegisterComponent
    },
    // {
    //     path:"**",
    //     component: PagenotfoundComponent,
    // }
]