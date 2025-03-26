import subprocess
import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import collections
import string

# Pastikan untuk mengunduh lexicon VADER jika belum
nltk.download('vader_lexicon')

def get_git_log():
    """
    Eksekusi perintah git untuk mendapatkan log commit dengan format:
    commit_hash|tanggal|pesan_commit
    """
    try:
        cmd = ["git", "log", "--pretty=format:%H|%ad|%s", "--date=iso"]
        output = subprocess.check_output(cmd).decode("utf-8")
        return output
    except Exception as e:
        print("Gagal mengambil log git. Pastikan Anda berada dalam direktori repository git.")
        print(e)
        exit(1)

def parse_git_log(log_output):
    data = []
    for line in log_output.splitlines():
        parts = line.split("|", 2)
        if len(parts) == 3:
            commit_hash, date_str, message = parts
            data.append({
                'commit_hash': commit_hash,
                'date': pd.to_datetime(date_str),
                'message': message
            })
    return pd.DataFrame(data)

def analyze_sentiments(df):
    sia = SentimentIntensityAnalyzer()
    df['sentiment'] = df['message'].apply(lambda msg: sia.polarity_scores(msg)['compound'])
    return df

def plot_commit_frequency(df):
    # Kelompokkan commit berdasarkan tanggal (tanpa waktu)
    commit_counts = df.groupby(df['date'].dt.date).size()
    plt.figure(figsize=(12,6))
    commit_counts.plot(kind='bar')
    plt.title("Frekuensi Commit per Hari")
    plt.xlabel("Tanggal")
    plt.ylabel("Jumlah Commit")
    plt.tight_layout()
    plt.show()

def plot_sentiment_distribution(df):
    plt.figure(figsize=(8,5))
    plt.hist(df['sentiment'], bins=20, edgecolor='black')
    plt.title("Distribusi Sentimen Pesan Commit")
    plt.xlabel("Skor Sentimen (Compound)")
    plt.ylabel("Frekuensi")
    plt.tight_layout()
    plt.show()

def analyze_word_frequency(df, top_n=10):
    words = []
    for msg in df['message']:
        # Hapus tanda baca dan ubah ke huruf kecil
        msg_clean = msg.translate(str.maketrans('', '', string.punctuation))
        words.extend(msg_clean.lower().split())
    word_counts = collections.Counter(words)
    common_words = word_counts.most_common(top_n)
    print("Kata-kata yang paling sering muncul dalam pesan commit:")
    for word, count in common_words:
        print(f"{word}: {count}")

def main():
    log_output = get_git_log()
    df = parse_git_log(log_output)
    
    if df.empty:
        print("Tidak ditemukan data commit.")
        return

    # Analisis sentimen pesan commit
    df = analyze_sentiments(df)

    # Tampilkan beberapa statistik
    print(f"Jumlah commit: {len(df)}")
    print(f"Sentimen rata-rata: {df['sentiment'].mean():.2f}")

    # Visualisasi data
    plot_commit_frequency(df)
    plot_sentiment_distribution(df)
    analyze_word_frequency(df)

if __name__ == "__main__":
    main()
