import { Component, OnInit, OnDestroy } from '@angular/core';
import { ApiService } from '../api.service';
import { Router, ActivatedRoute } from '@angular/router';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  providers: [ApiService]
})
export class LoginComponent implements OnInit, OnDestroy {
  private listSub: Subscription[] = [];
  public loginForm: FormGroup;
  public loading = false;
  returnUrl : string = "";

  constructor(
    private api: ApiService,
    private router: Router,
    private route: ActivatedRoute,
    private formBuilder: FormBuilder
  ) { }

  ngOnInit() {
    // this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
    this.createFormLogin();
  }

  createFormLogin() {
    
    this.loginForm = this.formBuilder.group({
      username: ['', [
        Validators.required,
        Validators.minLength(1),
        Validators.maxLength(20)
      ]],
      password: ['', [
        Validators.required
      ]]
    });
    this.loginForm.valueChanges.subscribe(data => {
      console.log(data);
      
    });
  }

  onLogin() {
    console.log(this.loginForm);
    let data = {
      username: this.loginForm.value.username,
      password: this.loginForm.value.password
    };
    console.log(data);
    this.loading = true;
    this.listSub.push(
      this.api.login(data).subscribe(
        token => {
          console.log(token);
          if(token) {
            this.loading = false;
            localStorage.setItem('token', token.key);
            // this.router.navigate([this.returnUrl]);
          }
          this.api.getCurrentUser().subscribe(
            data => {
              console.log(data);
              if(data.is_superuser == true) {
                this.router.navigate(['/home']);
              } else {
                this.router.navigate(['/']);
              }
            },
            error => {
              console.log(error);
            }
          )
        },
        error => {
          this.loading = false;
          console.log(error);
        }
      )
    );
  }

  ngOnDestroy(): void {
    this.listSub.forEach(sub => sub.unsubscribe());
  }
}
