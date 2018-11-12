@app.route('/reset/<token>', methods=['GET', 'POST'])
def reset_password_with_token(token):
    if current_user.is_authenticated():
        flash('You are already logged in.')
        return redirect(index_url_for_blueprint(current_user))
    user = User.query.filter_by(reset_token = token).first()
    if user is None:
        return abort(error)
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.new_password.data)
        flash('Your password was successfully changed.')
        login_user(user)
        user.reset_token = None
        return redirect(index_url_for_blueprint(current_user))        
    return render_template('app/reset_password.html', form=form)
