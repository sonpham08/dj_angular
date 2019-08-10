import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home.component';
import { ManageCategoryComponent } from '../manage-category/manage-category.component';
import { ManageProductComponent } from '../manage-product/manage-product.component';
import { AsideMenuComponent } from '../aside-menu/aside-menu.component';
import { SubHeaderComponent } from '../sub-header/sub-header.component';
import { AvatarModule } from 'ngx-avatar';

const appRoutes: Routes = [
  {
      path: "",
      // component: HomeComponent,
      children: [
          { path: '', redirectTo: '/home/product', pathMatch: 'full' },
          { path: 'home/product', component: HomeComponent },
          { path: 'home/category', component: ManageCategoryComponent },
      ]
  },
]

@NgModule({
  declarations: [
    HomeComponent,
    ManageCategoryComponent,
    ManageProductComponent,
    AsideMenuComponent,
    SubHeaderComponent,
  ],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    AvatarModule,
    RouterModule.forChild(appRoutes)
  ],
  exports: [
    HomeComponent, 
    ManageCategoryComponent, 
    ManageProductComponent,
    AsideMenuComponent,
  ],
})
export class HomeModule { }
