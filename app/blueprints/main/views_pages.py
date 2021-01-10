from .views import bp
from flask import render_template


@bp.route('/job-listing')
def page_job_listing():
    return render_template('pages/job-listing.html')


# note - will be replaced to fetch job details from database
@bp.route('/job-details')
def page_job_details():
    return render_template('pages/job-details.html')


@bp.route('/about-us')
def page_about_us():
    return render_template('pages/about-us.html')


@bp.route('/blog-home')
def page_blog_home():
    return render_template('pages/blog-posts.html')


# note - will be replaced to fetch blog post from database
@bp.route('/blog-post')
def page_blog_post():
    return render_template('pages/blog-post-details.html')


@bp.route('/team-home')
def page_team_home():
    return render_template('pages/team.html')


@bp.route('/testimonials')
def page_testimonials():
    return render_template('pages/testimonials.html')


@bp.route('/terms')
def page_terms():
    return render_template('pages/terms.html')


@bp.route('/contact')
def page_contact():
    return render_template('pages/contact.html')
