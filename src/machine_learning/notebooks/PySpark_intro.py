import marimo

__generated_with = "0.14.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pyspark as ps

    return (ps,)


@app.cell
def _(ps):
    spark = ps.sql.SparkSession.builder.appName("MarimoPySpark").getOrCreate()
    return


if __name__ == "__main__":
    app.run()
