import time
import random
import pandas as pd
from DrissionPage import ChromiumPage
import re
import uuid

def display_banner():
    banner = r"""
    ╔════════════════════════════════════════════════════╗
    ║         Facebook Comments Scraper v1.0             ║
    ║           For Khaadi Page Comments                ║
    ╚════════════════════════════════════════════════════╝
    """
    print("\033[1;36m" + banner + "\033[0m")

def scrape_facebook_comments():
    # Initialize browser session
    page = ChromiumPage()
    
    # Navigate to Khaadi Facebook page
    print("Navigating to Khaadi Facebook page...")
    page.get('https://web.facebook.com/khaadi')
    time.sleep(5)  # Wait for page to load

    # Prompt for manual login (automated login is risky and not recommended)
    input("\033[1;32mPlease log in to Facebook manually, then press Enter to continue...\033[0m")
    
    comments_data = []
    processed_post_ids = set()

    # Scroll to load posts
    print("Scrolling to load posts...")
    for _ in range(10):  # Adjust for more posts
        page.scroll.down(1500)
        page.scroll.to_bottom()
        time.sleep(random.uniform(1.5, 2.5))

    while True:
        # Find post elements
        post_elements = page.eles('xpath://div[contains(@class, "x1yztbdb") and contains(@class, "x1n2onr6")]', timeout=5)
        if not post_elements:
            print("No post elements found. Debugging page content...")
            login_prompt = page.ele('xpath://button[contains(text(), "Log In")]', timeout=2)
            if login_prompt:
                print("Login prompt detected. Please ensure you are logged in.")
                page.quit()
                return
            print("No posts found. Stopping...")
            break
        
        print(f"Found {len(post_elements)} post elements in this iteration")

        for post in post_elements:
            # Extract post ID
            post_id = str(uuid.uuid4())  # Generate unique ID (Facebook post IDs are complex)
            if post_id in processed_post_ids:
                continue
            processed_post_ids.add(post_id)

            # Click "View more comments" to load all comments
            try:
                view_more_comments = post.ele('xpath:.//span[contains(text(), "View more comments") or contains(text(), "View previous comments")]', timeout=2)
                while view_more_comments:
                    view_more_comments.click(by_js=True)
                    time.sleep(random.uniform(1, 2))
                    view_more_comments = post.ele('xpath:.//span[contains(text(), "View more comments") or contains(text(), "View previous comments")]', timeout=2)
            except Exception as e:
                print(f"Error loading more comments: {e}")

            # Extract comments
            try:
                comment_elements = post.eles('xpath:.//div[contains(@class, "x1n0m28w") and contains(@class, "x1vjfegm")]', timeout=2)
                for comment in comment_elements:
                    comment_details = {}
                    comment_details['Post_ID'] = post_id

                    # Extract commenter name
                    try:
                        name_element = comment.ele('xpath:.//span[contains(@class, "x3nfvp2")]', timeout=1)
                        comment_details['Commenter_Name'] = name_element.text.strip() if name_element else 'Unknown'
                    except:
                        comment_details['Commenter_Name'] = 'Unknown'

                    # Extract comment text
                    try:
                        text_element = comment.ele('xpath:.//div[contains(@class, "xdj266r")]', timeout=1)
                        comment_text = text_element.text.strip() if text_element else ''
                        comment_text = re.sub(r'\s+', ' ', comment_text)  # Clean whitespace
                        comment_details['Comment'] = comment_text if comment_text else 'No content'
                    except:
                        comment_details['Comment'] = 'No content'

                    # Extract timestamp (approximate, as exact timestamps are complex)
                    try:
                        time_element = comment.ele('xpath:.//span[contains(@class, "x4k7w5x")]', timeout=1)
                        comment_details['Timestamp'] = time_element.text.strip() if time_element else 'Unknown'
                    except:
                        comment_details['Timestamp'] = 'Unknown'

                    comments_data.append(comment_details)
                    print(f"Scraped comment: {comment_details['Comment'][:50]}... by {comment_details['Commenter_Name']}")
            except Exception as e:
                print(f"Error extracting comments for post {post_id}: {e}")

        # Check for "Show more results" or load more posts
        show_more_button = page.ele('xpath://span[contains(text(), "See more stories") or contains(text(), "Show more")]', timeout=5)
        if show_more_button:
            print("Show more posts button found, clicking...")
            try:
                show_more_button.click(by_js=True)
                time.sleep(random.uniform(2, 4))
                for _ in range(5):
                    page.scroll.to_bottom()
                    time.sleep(1.5)
            except Exception as e:
                print(f"Error clicking show more button: {e}")
                break
        else:
            print("No more posts to load. Stopping...")
            break

    # Save comments to CSV
    if comments_data:
        df = pd.DataFrame(comments_data, columns=['Post_ID', 'Commenter_Name', 'Comment', 'Timestamp'])
        df.to_csv('khaadi_comments.csv', index=False, encoding='utf-8')
        print(f"Exported {len(comments_data)} comments to khaadi_comments.csv")
    else:
        print("No comments found to export.")

    page.quit()

def main():
    display_banner()
    scrape_facebook_comments()

if __name__ == "__main__":
    main()