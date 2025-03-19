def create_subject_query(subject, post_content):
    subject = subject.lower()
    
    post_content = post_content.replace("'", "''")
    
    return f"""
    UPDATE wp_posts
    SET post_content = '{post_content}'
    WHERE LOWER(post_title) LIKE '%{subject}%' 
    AND post_status = 'draft'
    AND (SELECT COUNT(*) 
        FROM wp_posts 
        WHERE LOWER(post_title) LIKE '%{subject}%' 
            AND post_status = 'draft') = 1;
    """
