--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

-- Started on 2024-03-10 01:37:27

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 33689)
-- Name: Users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Users" (
    user_id bigint NOT NULL,
    username character varying(32) NOT NULL
);


ALTER TABLE public."Users" OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 33699)
-- Name: UsersDeferredBooks; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."UsersDeferredBooks" (
    user_id bigint NOT NULL,
    book_id integer NOT NULL
);


ALTER TABLE public."UsersDeferredBooks" OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 33694)
-- Name: UsersReadBooks; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."UsersReadBooks" (
    user_id bigint NOT NULL,
    book_id integer NOT NULL
);


ALTER TABLE public."UsersReadBooks" OWNER TO postgres;

--
-- TOC entry 4790 (class 0 OID 33689)
-- Dependencies: 215
-- Data for Name: Users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Users" (user_id, username) FROM stdin;
\.


--
-- TOC entry 4792 (class 0 OID 33699)
-- Dependencies: 217
-- Data for Name: UsersDeferredBooks; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."UsersDeferredBooks" (user_id, book_id) FROM stdin;
\.


--
-- TOC entry 4791 (class 0 OID 33694)
-- Dependencies: 216
-- Data for Name: UsersReadBooks; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."UsersReadBooks" (user_id, book_id) FROM stdin;
\.


--
-- TOC entry 4646 (class 2606 OID 33703)
-- Name: UsersDeferredBooks UsersDeferredBooks_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."UsersDeferredBooks"
    ADD CONSTRAINT "UsersDeferredBooks_pkey" PRIMARY KEY (user_id, book_id);


--
-- TOC entry 4644 (class 2606 OID 33698)
-- Name: UsersReadBooks UsersReadBooks_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."UsersReadBooks"
    ADD CONSTRAINT "UsersReadBooks_pkey" PRIMARY KEY (book_id, user_id);


--
-- TOC entry 4642 (class 2606 OID 33693)
-- Name: Users Users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Users"
    ADD CONSTRAINT "Users_pkey" PRIMARY KEY (user_id);


-- Completed on 2024-03-10 01:37:27

--
-- PostgreSQL database dump complete
--

